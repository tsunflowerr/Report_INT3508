"""Publication figures from the verified, complete recorded observations only.

Backend: Python/matplotlib; editable vector exports at 160 mm final width.
All marks are descriptive. No invented intervals, tests, or simulated observations.
Service figure: budget categories, exact totals across all 20 matched cells/window.
Gates figure: 8 matched development cells per window, observed vs sealed predictions.
T38 figures: all 34 test episodes for paired differences; all 49 C-30 episodes for scores.
"""
from pathlib import Path
import collections, csv, json, statistics, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib import font_manager

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SKILL = ROOT.parent/'nature-skills-audit-2026-10-04'/'skills'/'nature-figure'
sys.path.insert(0, str(SKILL/'scripts'))
from audit_panel_alignment import require_matplotlib_panel_alignment

OUTPUT = ROOT/'source'/'hinh'
QA = HERE/'figures'
OUTPUT.mkdir(parents=True,exist_ok=True)
QA.mkdir(parents=True,exist_ok=True)
WIDTH_MM = 160
INK = '#292929'
BLUE = '#345f87'
OCHRE = '#946934'
GREY = '#737373'
RULE = '#dedede'
plt.rcParams.update({'font.family':'serif','font.serif':['Times New Roman','STIXGeneral','DejaVu Serif'],
    'mathtext.fontset':'stix','font.size':11,'axes.labelsize':11,'axes.titlesize':12,
    'xtick.labelsize':11,'ytick.labelsize':11,'legend.fontsize':11,
    'pdf.fonttype':42,'svg.fonttype':'none','text.color':INK,'axes.labelcolor':INK,
    'xtick.color':INK,'ytick.color':INK,'axes.edgecolor':GREY,
    'axes.spines.right':False,'axes.spines.top':False,'axes.linewidth':0.7,
    'savefig.facecolor':'white','figure.facecolor':'white'})

def style(ax, grid=True):
    ax.set_axisbelow(True)
    if grid:
        ax.grid(axis='y',color=RULE,linewidth=0.6)
    ax.tick_params(length=3,width=0.6)

def finish(fig,name):
    fig.canvas.draw()
    require_matplotlib_panel_alignment(fig,json_out=QA/f'{name}.alignment.json',
        overlay_svg=QA/f'{name}.alignment.svg',tolerance_pt=1.5,gutter_tolerance_pt=1.5,strict=True)
    # Preserve the designed 160 mm page box: no tight bounding-box crop changes size.
    fig.savefig(OUTPUT/f'{name}.pdf',format='pdf')
    fig.savefig(OUTPUT/f'{name}.svg',format='svg')
    fig.savefig(QA/f'{name}.png',dpi=300)
    plt.close(fig)
    print(name,'exported',flush=True)

def service_budget():
    rows=list(csv.DictReader((HERE/'service-budget-summary.csv').open(encoding='utf-8')))
    order=['c1','budget60','budget120','budget300','nobudget']
    fig,ax=plt.subplots(figsize=(WIDTH_MM/25.4,88/25.4))
    fig.subplots_adjust(left=0.15,right=0.975,bottom=0.20,top=0.81)
    for window,color,marker,line,label in [(600,BLUE,'o','-','Cửa sổ đón 600 s'),(900,OCHRE,'s','--','Cửa sổ đón 900 s')]:
        mine={r['arm']:r for r in rows if int(r['windowSeconds'])==window}
        assert all(int(mine[a]['cells'])==20 and int(mine[a]['requests'])==2160 for a in order)
        y=[float(mine[a]['lossPp']) for a in order]
        ax.plot(range(5),y,color=color,marker=marker,linestyle=line,markersize=6,linewidth=1.5,label=label)
    ax.set_xticks(range(5),['30','60','120','300','Không trần'])
    ax.set_xlim(-0.25,4.35)
    ax.set_ylim(3.0,9.0)
    ax.set_yticks([3,4,5,6,7,8,9])
    ax.set_xlabel('Trần cộng dồn độ dời giờ trả do quyết định (s)',labelpad=8)
    ax.set_ylabel('Giảm tỉ lệ phục vụ so với B1\n(điểm phần trăm)',labelpad=8)
    fig.legend(*ax.get_legend_handles_labels(),loc='upper center',bbox_to_anchor=(0.56,0.97),ncol=1,frameon=False)
    style(ax)
    finish(fig,'service_budget_final')

def gates():
    sys.path.insert(0,str(ROOT.parent/'deadline'))
    import classify,run_deadline as rd
    predictions=list(csv.DictReader((ROOT.parent/'deadline'/'predictions.csv').open(encoding='utf-8')))
    families=[('C','conduct-30'),('M+','dl-30'),('M','dl2-30'),('V','visible-30')]
    rows=[]
    fig,axes=plt.subplots(1,2,figsize=(WIDTH_MM/25.4,92/25.4),sharey=True)
    fig.subplots_adjust(left=0.13,right=0.975,bottom=0.19,top=0.77,wspace=0.24)
    for i,(ax,window,title) in enumerate(zip(axes,('w08','w17'),('08:00–10:00','17:00–19:00'))):
        cells=[c for c in rd.PANEL_DEV['cells'] if c.endswith(window)]
        assert len(cells)==8
        observed,predicted=[],[]
        for label,arm in families:
            statuses=[classify.classify_output(rd.effective_output(f'{arm}-k1-{c}-s7')) for c in cells]
            assert all(s not in ('pending','no-artifact','other') for s in statuses)
            n=sum(classify.is_commitment_infeasible(s) for s in statuses)
            mine=[r for r in predictions if r['stage']=='2b' and r['arm']==arm and r['window']==window]
            p=sum(r['prediction']=='commitment-infeasible' for r in mine)
            assert len(mine)==8 or arm=='conduct-30'
            observed.append(n/8);predicted.append(p/8)
            rows.append({'window':window,'family':label,'n':8,'observedFailures':n,'sealedPredictedFailures':p,
                'predictionType':'theorem' if arm=='conduct-30' else 'sealed-row-rule'})
        xs=list(range(4))
        ax.bar(xs,observed,width=.58,color='#aabccd',edgecolor=BLUE,linewidth=.8,label='Quan sát',zorder=2)
        ax.scatter(xs,predicted,s=44,color=INK,marker='D',zorder=3,label='Dự đoán')
        for x,n in zip(xs,[int(8*v) for v in observed]):
            ax.text(x,n/8+.075,f'{n}/8',ha='center',va='bottom',fontsize=11)
        ax.set_xticks(xs,[f[0] for f in families],fontsize=12)
        ax.set_xlim(-.55,3.55);ax.set_ylim(-.08,1.22)
        ax.set_yticks([0,.25,.5,.75,1.0],['0','25','50','75','100'])
        ax.set_title(title,pad=10)
        ax.text(-.08,1.17,chr(97+i),transform=ax.transAxes,weight='bold',fontsize=12,ha='left',va='top')
        style(ax,grid=False)
    axes[0].set_ylabel('Ô vô nghiệm do cam kết (%)',labelpad=7)
    fig.supxlabel('Họ cổng, cùng mức 30 s',y=.025,fontsize=11)
    handles,names=axes[0].get_legend_handles_labels()
    fig.legend(handles,names,loc='upper center',bbox_to_anchor=(.56,.99),ncol=2,frameon=False)
    with (HERE/'tier2-gates-figure-data.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    finish(fig,'tier2_gates_final')

def paired_t38():
    raw=json.loads((HERE/'t38-raw-checkpoint-recheck.json').read_text(encoding='utf-8'))['runs']
    tests=[r for r in raw if r['phase']=='test']
    by={(r['arm'],r['cell']):r for r in tests}
    cells=[r['cell'] for r in tests if r['arm']=='C-30']
    assert len(cells)==34
    columns=[('C − M+',lambda c:by[('C-30',c)]['served']-by[('Mplus-30',c)]['served']),
        ('C − V',lambda c:by[('C-30',c)]['served']-by[('V-30',c)]['served']),
        ('U − C',lambda c:by[('U',c)]['served']-by[('C-30',c)]['served'])]
    windows=[('w07','07:00–09:00',BLUE,'o'),('w08','08:00–10:00',OCHRE,'s'),('w17','17:00–19:00',GREY,'^')]
    fig,ax=plt.subplots(figsize=(WIDTH_MM/25.4,94/25.4))
    fig.subplots_adjust(left=.14,right=.975,bottom=.19,top=.78)
    for x,(label,fn) in enumerate(columns):
        allvals=[fn(c) for c in cells]
        for wi,(window,display,color,marker) in enumerate(windows):
            mine=[c for c in cells if c.endswith(window)]
            # Deterministic displacement only reveals coincident integer observations;
            # it is not a resampling or uncertainty estimate.
            for j,c in enumerate(mine):
                offset=-.25+.13*wi+.012*(j%5-2)
                ax.scatter(x+offset,fn(c),s=29,marker=marker,facecolor=color,edgecolor='white',linewidth=.35,zorder=3)
        mean=statistics.mean(allvals)
        ax.scatter(x+.23,mean,s=66,marker='D',facecolor='white',edgecolor=INK,linewidth=1.0,zorder=4)
    ax.axhline(0,color=INK,linewidth=.8,zorder=1)
    ax.set_xticks(range(3),[c[0] for c in columns],fontsize=12)
    ax.set_xlim(-.6,2.65);ax.set_ylim(-5,10)
    ax.set_yticks([-4,-2,0,2,4,6,8,10])
    ax.set_ylabel('Chênh số khách hoàn tất trong cùng ô',labelpad=8)
    ax.set_xlabel('C, M+ và V cùng mức 30 s; U không đặt trần',labelpad=8)
    handles=[Line2D([],[],marker=m,color=c,linestyle='None',markersize=5,label=d) for w,d,c,m in windows]
    handles.append(Line2D([],[],marker='D',markerfacecolor='white',markeredgecolor=INK,color=INK,linestyle='None',markersize=6,label='Trung bình 34 ô'))
    fig.legend(handles=handles,loc='upper center',bbox_to_anchor=(.55,.99),ncol=2,frameon=False,columnspacing=1.3)
    style(ax)
    finish(fig,'t38_paired_final')

def scores_t38():
    raw=json.loads((HERE/'t38-raw-checkpoint-recheck.json').read_text(encoding='utf-8'))
    rows=[r for r in raw['runs'] if r['arm']=='C-30']
    assert len(rows)==49
    gamma=raw['summary']['gammaMs']/1000
    windows=[('w07','07:00–09:00'),('w08','08:00–10:00'),('w17','17:00–19:00')]
    fig,ax=plt.subplots(figsize=(WIDTH_MM/25.4,90/25.4))
    fig.subplots_adjust(left=.14,right=.975,bottom=.19,top=.84)
    for x,(window,display) in enumerate(windows):
        for phase,shift,color,marker in [('calib',-.16,OCHRE,'s'),('test',.16,BLUE,'o')]:
            mine=[r for r in rows if r['cell'].endswith(window) and r['phase']==phase]
            for j,r in enumerate(mine):
                ax.scatter(x+shift+.018*(j%5-2),r['scoreMs']/1000,s=31,facecolor=color,edgecolor='white',linewidth=.4,marker=marker,zorder=3)
    ax.axhline(gamma,color=INK,linestyle='--',linewidth=1,zorder=2)
    ax.text(1.12,gamma+7,'γ = 222,259 s',ha='center',va='bottom',fontsize=11)
    ax.set_xticks(range(3),[w[1] for w in windows])
    ax.set_xlim(-.6,2.6);ax.set_ylim(0,285)
    ax.set_yticks([0,50,100,150,200,250])
    ax.set_ylabel('Điểm giữ tuyến S theo ô (s)',labelpad=8)
    ax.set_xlabel('Khung giờ thực nghiệm',labelpad=8)
    handles=[Line2D([],[],marker='s',color=OCHRE,linestyle='None',markersize=6,label='Hiệu chỉnh: 15 ô'),
        Line2D([],[],marker='o',color=BLUE,linestyle='None',markersize=6,label='Kiểm tra: 34 ô')]
    fig.legend(handles=handles,loc='upper center',bbox_to_anchor=(.56,.98),ncol=2,frameon=False)
    style(ax)
    finish(fig,'t38_scores_final')

if __name__=='__main__':
    print('Font:',font_manager.findfont('Times New Roman'),flush=True)
    service_budget();gates();paired_t38();scores_t38()
