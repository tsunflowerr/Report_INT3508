"""Audit actual original taxi-trip identities across the existing T38 split.

No experiment is run. Source files, fixtures and split are read only.
StrictCsv.cs uses zero-based ordinals after the header. Ordinals are local to
each demand CSV, so they cannot identify trips across sample files. Instead
this audit reads the CSV's original request_id and checks timestamp/OD equality.
"""
from pathlib import Path
import csv, hashlib, json

HERE = Path(__file__).resolve().parent
FIXTURES = Path(r'C:\RideBoundData\research\fixtures-panelA-v1')
SPLIT = Path(r'E:\Code\Report_INT3508\ridebound-scratchpad\tang3\t38\split-t38-v1.json')
ARCHIVE = Path(r'E:\RideBoundData\wp6\extracted\sha256\d9\d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e')
manifest = json.loads(SPLIT.read_text(encoding='utf-8'))
files = {}
trip_sets = {}
episode_sources = []
source_values = {}
for cell in manifest['calibration'] + manifest['test']:
    config_path = FIXTURES / cell / 'normalizer-configuration.json'
    config = json.loads(config_path.read_text(encoding='utf-8'))
    member = config['demandMemberPath']
    if member not in files:
        path = ARCHIVE / member
        with path.open(encoding='utf-8', newline='') as handle:
            files[member] = list(csv.DictReader(handle))
    selections = json.loads((FIXTURES / cell / 'selection-frame.json').read_text(encoding='utf-8'))
    ordinals = {row['sourceRecordOrdinal'] for row in selections if row['disposition'] == 'selected'}
    assert len(ordinals) == 108
    trips = {}
    selected = []
    for ordinal in sorted(ordinals):
        row = files[member][ordinal]
        assert config['sourceWindowStartSeconds'] <= int(row['rq_time']) < config['sourceWindowEndSeconds']
        key = (config['sourceLocalDate'], row['request_id'])
        value = (row['rq_time'], row['start'], row['end'])
        if key in source_values:
            assert source_values[key] == value, ('same ID with differing source values', key)
        source_values[key] = value
        trips[key] = value
        selected.append({'ordinal': ordinal, 'originalRequestId': row['request_id'],
                         'rqTimeSeconds': row['rq_time'], 'start': row['start'], 'end': row['end']})
    assert len(trips) == 108
    trip_sets[cell] = trips
    episode_sources.append({'cell': cell, 'phase': 'calib' if cell in manifest['calibration'] else 'test',
                            'demandMemberPath': member, 'selectedTrips': selected})

calibration = set.union(*(set(trip_sets[cell]) for cell in manifest['calibration']))
test = set.union(*(set(trip_sets[cell]) for cell in manifest['test']))
overlap = calibration & test
pairs = []
for c in manifest['calibration']:
    for t in manifest['test']:
        shared = set(trip_sets[c]) & set(trip_sets[t])
        if shared:
            assert all(trip_sets[c][key] == trip_sets[t][key] for key in shared)
            pairs.append({'calib': c, 'test': t, 'sharedTrips': len(shared),
                          'sourceRequestIds': [list(key) for key in sorted(shared)]})
days = sorted({key[0] for key in overlap})
output = {
    'status': 'VERIFIED_WITH_ORIGINAL_CSV_REQUEST_ID',
    'identifier': '(sourceLocalDate, original CSV request_id)',
    'ordinalConvention': 'zero-based data-record ordinal, header excluded, local to demandMemberPath',
    'assertions': '108 selected unique IDs per episode; times inside configured window; repeated original IDs have identical rq_time/start/end',
    'splitPath': str(SPLIT),
    'splitSha256': hashlib.sha256(SPLIT.read_bytes()).hexdigest(),
    'sourceCsvCount': len(files),
    'calibrationEpisodeCount': len(manifest['calibration']),
    'testEpisodeCount': len(manifest['test']),
    'calibrationTripsUnique': len(calibration),
    'testTripsUnique': len(test),
    'crossPartitionOverlapUnique': len(overlap),
    'nonzeroEpisodePairs': len(pairs),
    'byDay': [{'day': day, 'overlap': sum(key[0] == day for key in overlap)} for day in days],
    'pairs': pairs,
    'crosspartitionTrips': [list(key) for key in sorted(overlap)],
    'sourceCsvSha256': {member: hashlib.sha256((ARCHIVE / member).read_bytes()).hexdigest() for member in files},
    'episodeSources': episode_sources,
}
(HERE / 't38-actual-trip-id-overlap.json').write_text(json.dumps(output, indent=1), encoding='utf-8')
print(json.dumps({k: output[k] for k in ('status','sourceCsvCount','calibrationTripsUnique','testTripsUnique','crossPartitionOverlapUnique','nonzeroEpisodePairs','byDay')}, indent=2))

# Preserve the earlier ordinal-only diagnostic and explicitly mark why it is invalid.
obsolete_path = HERE / 't38-source-row-overlap.json'
if obsolete_path.exists():
    obsolete = json.loads(obsolete_path.read_text(encoding='utf-8'))
    obsolete['status'] = 'INVALID_IDENTIFIER_DIAGNOSTIC_DO_NOT_CITE'
    obsolete['reason'] = 'SourceRecordOrdinal is local to each different sample demand CSV. Day plus ordinal is not a trip identity.'
    obsolete['supersededBy'] = 't38-actual-trip-id-overlap.json'
    obsolete_path.write_text(json.dumps(obsolete, indent=1), encoding='utf-8')
