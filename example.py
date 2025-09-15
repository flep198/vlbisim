import vlbi_sim
from vlbi_sim import Telescope
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.rcParams.update({
    "text.usetex": False,
    "font.family": "Quicksand"
})

#load existing array
eht=vlbi_sim.getArray("eht")

for tel in eht:
    print(tel)

#add custom telescope
eht.append(Telescope(-10.0,10.0,name="custom",elev_lim=20))

for tel in eht:
    print(tel)

#Define Source coordinates in RA/Dec or hourangle or degrees works both
source=["05:09:25.9645434784","05:41:35.333636817"]

fit=plt.figure(figsize=(8,8))
uv_coverages=vlbi_sim.simulateUV(eht,source,n_iter=10000,obsstart=0,obsend=24,obsday="2025-04-01",plotLim=18000)
highlight_baselines=vlbi_sim.getHighlightBaselines(eht,names=["ALMA"])
highlight_baselines2=vlbi_sim.getHighlightBaselines(eht,names=["custom"])
vlbi_sim.plotUVdata(uv_coverages,highlight_baselines=[highlight_baselines,highlight_baselines2],baseline_colors=["black","red","green"],wavelength=1.3e-6)

plt.axis('equal')
    
colors = ["red"]
lines = [Line2D([0], [0], color=c, linewidth=3, linestyle='-') for c in colors]
labels = ['ALMA baselines']
plt.legend(lines, labels,fontsize=16)
    
plt.tight_layout()    
plt.savefig("0506_056_uv_EHT.png",dpi=300)
plt.show()
