"""Convert a RideBound H6 fixture into a stock-FleetPy study, then run it.

Purpose: bound the cost of RideBound's structural vehicle lock by comparing its
service rate against stock FleetPy fleet controls (AlonsoMora / InsertionHeuristic)
on the SAME network, the SAME 108 requests, the SAME 8 vehicles of capacity 4 and
the SAME service-level constraints.

Nothing in the RideBound repository is written. The generated FleetPy study lives
under the FleetPy install (additive data + studies folders only; no source edits).
"""

from __future__ import annotations

import argparse
import csv
import json
import pathlib
import sys

FLEETPY = pathlib.Path(r"E:/RideBoundData/wp7/FleetPy-1.0.2")
REPO = pathlib.Path(r"E:/Code/RideBound")
FIXTURE_ROOT = REPO / (
    "benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/"
    "wp9-confirmatory-fixed-panel-v2"
)

# FleetPy derives the study name from the directory that holds `scenarios/`,
# so this must match the scratchpad folder this script lives in.
STUDY = "calib"


def load_source(cell):
    path = FIXTURE_ROOT / cell / "scenario-content.json"
    return json.loads(path.read_text(encoding="utf-8"))


def node_index_of(source):
    """Same ordering the RideBound preflight uses, so node ids line up exactly."""
    arcs = source["travelSnapshots"][0]["arcs"]
    nodes = sorted(
        {arc["fromNodeId"] for arc in arcs} | {arc["toNodeId"] for arc in arcs}
    )
    return {node_id: index for index, node_id in enumerate(nodes)}, nodes


def write_network(network_name, source, index, nodes):
    base = FLEETPY / "data" / "networks" / network_name / "base"
    base.mkdir(parents=True, exist_ok=True)
    with (base / "nodes.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["node_index", "is_stop_only", "pos_x", "pos_y"])
        for i, _node in enumerate(nodes):
            w.writerow([i, "True", i * 1000, 0])
    arcs = source["travelSnapshots"][0]["arcs"]
    with (base / "edges.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(
            ["from_node", "to_node", "distance", "travel_time", "source_edge_id"]
        )
        for ordinal, arc in enumerate(arcs):
            seconds = arc["travelTimeMs"] / 1000
            w.writerow(
                [
                    index[arc["fromNodeId"]],
                    index[arc["toNodeId"]],
                    seconds * 10,
                    seconds,
                    ordinal,
                ]
            )
    (base / "crs.info").write_text("EPSG:32632\n", encoding="ascii")
    return base


def write_demand(demand_name, network_name, rq_file, source, index):
    directory = (
        FLEETPY / "data" / "demand" / demand_name / "matched" / network_name
    )
    directory.mkdir(parents=True, exist_ok=True)
    rows = []
    for ordinal, request in enumerate(
        sorted(source["requests"], key=lambda r: (r["arrivalTimeMs"], r["requestId"]))
    ):
        rows.append(
            {
                "rq_time": request["arrivalTimeMs"] // 1000,
                "start": index[request["originNodeId"]],
                "end": index[request["destinationNodeId"]],
                "request_id": ordinal,
            }
        )
    path = directory / rq_file
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(
            fh, fieldnames=["rq_time", "start", "end", "request_id"],
            lineterminator="\n",
        )
        w.writeheader()
        w.writerows(rows)
    return path, len(rows)


def write_initial_state(init_scenario, source, index):
    """Pin FleetPy's vehicles to the exact nodes the RideBound fixture uses.

    Without this FleetPy scatters vehicles uniformly at random, which is not the
    same starting fleet and would make the service-rate comparison meaningless.
    """
    directory = FLEETPY / "studies" / STUDY / "results" / init_scenario
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / "final_state.csv"
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(
            ["", "operator_id", "vehicle_id", "final_soc",
             "final_node_index", "final_time"],
        )
        for vid, vehicle in enumerate(source["fleet"]):
            position = vehicle["position"]
            if position.get("kind") != "node":
                raise RuntimeError(
                    f"vehicle {vid} does not start on a node: {position}"
                )
            w.writerow([vid, 0, vid, 1.0, index[position["nodeId"]], 0])
    return path, len(source["fleet"])


CONST_TEMPLATE = """sim_env: BatchOfferSimulation
initial_state_scenario: {init_scenario}
log_level: warning
network_type: NetworkBasic
network_name: {network_name}
demand_name: {demand_name}
random_seed: 7
start_time: 0
end_time: {end_time}
time_step: {time_step}
user_max_decision_time: 0
route_output_flag: False
replay_flag: False
nr_mod_operators: 1
rq_type: BasicRequest
study_name: {study}
op_module: RidePoolingBatchAssignmentFleetcontrol
op_rp_batch_optimizer: {optimizer}
op_vr_control_func_dict: {{func_key: total_system_time}}
op_min_wait_time: 0
op_max_wait_time: {max_wait}
op_max_detour_time_factor: {detour_factor}
op_const_boarding_time: 0
op_add_boarding_time: 0
op_base_fare: 0
op_distance_fare: 0
op_time_fare: 0
op_min_standard_fare: 0
op_reoptimisation_timestep: {time_step}
"""


def write_configs(scratch, network_name, demand_name, rq_file, optimizer,
                  scenario_name, fleet_size, end_time, time_step,
                  max_wait, detour_factor, init_scenario):
    scenarios = scratch / "scenarios"
    scenarios.mkdir(parents=True, exist_ok=True)
    const = scenarios / f"const_{scenario_name}.yaml"
    const.write_text(
        CONST_TEMPLATE.format(
            network_name=network_name,
            demand_name=demand_name,
            study=STUDY,
            optimizer=optimizer,
            end_time=end_time,
            time_step=time_step,
            max_wait=max_wait,
            detour_factor=detour_factor,
            init_scenario=init_scenario,
        ),
        encoding="utf-8",
    )
    sc = scenarios / f"scenario_{scenario_name}.csv"
    with sc.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["scenario_name", "rq_file", "op_fleet_composition"])
        w.writerow([scenario_name, rq_file, f"default_vehtype:{fleet_size}"])
    return const, sc


def summarize(scenario_name):
    results = FLEETPY / "studies" / STUDY / "results" / scenario_name
    if not results.exists():
        return {"error": f"no results directory at {results}"}
    files = sorted(p.name for p in results.iterdir())
    summary = {"resultsDir": str(results), "files": files}
    user_stats = results / "1_user-stats.csv"
    if user_stats.exists():
        served = 0
        total = 0
        with user_stats.open("r", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                total += 1
                operator = row.get("operator_id", "")
                if operator not in ("", "-1", "None"):
                    served += 1
        summary["totalRequests"] = total
        summary["served"] = served
        summary["rejected"] = total - served
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell", required=True)
    parser.add_argument(
        "--optimizer", default="AlonsoMora",
        choices=["AlonsoMora", "InsertionHeuristic", "SimonettoAssignment"],
    )
    parser.add_argument("--fleet-size", type=int, default=8)
    parser.add_argument("--time-step", type=int, default=30)
    parser.add_argument("--build-only", action="store_true")
    arguments = parser.parse_args()

    scratch = pathlib.Path(__file__).resolve().parent
    source = load_source(arguments.cell)
    index, nodes = node_index_of(source)

    network_name = f"ridebound_{arguments.cell.replace('-', '_')}"
    demand_name = f"ridebound_{arguments.cell.replace('-', '_')}_demand"
    rq_file = "requests.csv"
    scenario_name = f"{arguments.cell.replace('-', '_')}_{arguments.optimizer}"

    end_time = source["timeWindow"]["drainEndMs"] // 1000

    init_scenario = f"init_{arguments.cell.replace('-', '_')}"
    write_network(network_name, source, index, nodes)
    _, fleet_pinned = write_initial_state(init_scenario, source, index)
    _, request_count = write_demand(
        demand_name, network_name, rq_file, source, index
    )

    # RideBound encodes the ride-time cap as maxRideTime = factor x direct time.
    arcs = {
        (a["fromNodeId"], a["toNodeId"]): a["travelTimeMs"]
        for a in source["travelSnapshots"][0]["arcs"]
    }
    factors = {
        round(r["maxRideTimeMs"] / arcs[(r["originNodeId"], r["destinationNodeId"])], 4)
        for r in source["requests"]
        if (r["originNodeId"], r["destinationNodeId"]) in arcs
    }
    if len(factors) != 1:
        raise RuntimeError(f"ride-time factor is not uniform: {sorted(factors)[:5]}")
    detour_factor = round((factors.pop() - 1.0) * 100)

    windows = {
        r["latestPickupMs"] - r["earliestPickupMs"] for r in source["requests"]
    }
    if len(windows) != 1:
        raise RuntimeError(f"pickup window is not uniform: {sorted(windows)[:5]}")
    max_wait = windows.pop() // 1000

    const, sc = write_configs(
        scratch, network_name, demand_name, rq_file, arguments.optimizer,
        scenario_name, fleet_pinned, end_time, arguments.time_step,
        max_wait, detour_factor, init_scenario,
    )

    print(f"cell            : {arguments.cell}")
    print(f"requests        : {request_count}")
    print(f"nodes / arcs    : {len(nodes)} / {len(source['travelSnapshots'][0]['arcs'])}")
    print(f"fleet           : {fleet_pinned} x capacity 4 (positions pinned to fixture)")
    print(f"max wait (s)    : {max_wait}")
    print(f"detour factor % : {detour_factor}")
    print(f"end time (s)    : {end_time}")
    print(f"optimizer       : {arguments.optimizer}")
    print(f"const cfg       : {const}")
    print(f"scenario cfg    : {sc}", flush=True)

    if arguments.build_only:
        return 0

    sys.path.insert(0, str(FLEETPY))
    from run_scenarios import run_scenarios

    run_scenarios(str(const), str(sc), log_level="warning",
                  n_cpu_per_sim=1, n_parallel_sim=1)

    print()
    print(json.dumps(summarize(scenario_name), indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
