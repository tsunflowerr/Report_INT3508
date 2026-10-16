from pathlib import Path
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT.parent / 'nature-skills-audit-2026-10-04' / 'skills' / 'nature-figure' / 'scripts'
sys.path.insert(0, str(SKILL))
from audit_panel_alignment import require_matplotlib_panel_alignment

# Constructed example, not experimental observations. Positions preserve the 0/40/70 ratio.
plt.rcParams.update({'font.family':'Times New Roman','font.size':12,
                     'pdf.fonttype':42,'svg.fonttype':'none'})
fig, ax = plt.subplots(figsize=(160/25.4,70/25.4))
fig.subplots_adjust(left=.07,right=.93,bottom=.08,top=.94)
ax.set_xlim(-14,84)
ax.set_ylim(-.22,1.25)
ax.axis('off')
ax.plot([0,70],[.72,.72],color='#6c737b',linewidth=1.1)
for x, name, clock, marker in [(0,'v: đã công bố','9:10:00','o'),
                              (40,'e: giữ tuyến','9:10:40','s'),
                              (70,'p: phương án mới','9:11:10','^')]:
    ax.scatter([x],[.72],s=58,marker=marker,color='#173f68',zorder=3)
    ax.text(x,.98,name,ha='center',va='center')
    ax.text(x,.53,clock,ha='center',va='center')
for left,right,y,label in [(0,40,.29,'x = 40 s'),(40,70,.29,'c = 30 s'),(0,70,-.01,'z = 70 s')]:
    ax.annotate('',xy=(right,y),xytext=(left,y),
                arrowprops={'arrowstyle':'<->','color':'#505861','lw':1})
    ax.text((left+right)/2,y-.12,label,ha='center',va='center')
require_matplotlib_panel_alignment(fig,json_out=str(ROOT/'audit/mechanism-alignment.json'),
                                   tolerance_pt=1.5,strict=True)
out=ROOT/'source/hinh/co-che-ba-moc'
fig.savefig(str(out)+'.pdf')
fig.savefig(str(out)+'.svg')
fig.savefig(str(out)+'.png',dpi=200)
plt.close(fig)
