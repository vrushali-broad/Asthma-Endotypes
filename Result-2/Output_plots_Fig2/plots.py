#plot the simulations
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from pylab import *
import matplotlib as mpl
import seaborn as sns
import pandas as pd
#sns.set()
#sns.set(style="whitegrid")

runs = 350 #numseries
cycles = 800  #nummeasurements

# Basal
# Mild
# Medial
# Moderate --> df = pd.read_csv("../Simulation_output/stim_tmp_1_0.txt",sep ='\t') 
# Severe -->
fname = '../All_plots/Minimal.pdf'
df = pd.read_csv("../Output/Minimal.txt",sep ='\t')
df = df.T

print(df.shape, df.head())


df_dict = {}
for name in df.columns:
    row = np.mean(np.array(df[name]).reshape(runs,cycles), axis = 0)
    df_dict[name] = row


data = pd.DataFrame(df_dict)

plt.figure()
data_sub = data[['Eosinophils','Neutrophils','Basophils','Th2', 'Th17', 'Th1', 'Treg', 'Stimulant_I', 'Stimulant_II', 'Stimulant_III']]
legend_labels = ['Eosinophils','Neutrophils','Basophils','T$_\mathrm{H}$2', 'T$_\mathrm{H}$17', 'T$_\mathrm{H}$1', 'T$-$reg',
				'Stimulant T$_\mathrm{H}$2', 'Stimulant T$_\mathrm{H}$17', 'Stimulant T$_\mathrm{H}$1',]
data_sub.plot(style=['.-','.-'], lw=4, markeredgecolor='k',mew=10, markevery=50, legend=None)

plt.ylim([0,1])
plt.xlim(left=0)
plt.xticks(fontsize=17, fontweight = 'bold')
plt.yticks(fontsize=17, fontweight = 'bold')
plt.xlabel('Time Steps',  fontsize=20, fontweight = 'bold')
plt.ylabel('Node Activity',  fontsize=20, fontweight = 'bold')
plt.tight_layout()

plt.savefig(fname,bbox_inches='tight')

## Plot legend separately
axes = plt.gca()
figsize = (3, 3)
fig_leg = plt.figure(figsize=figsize)
ax_leg = fig_leg.add_subplot(111)
#ax_leg.legend(*axes.get_legend_handles_labels(), loc='center')

h,l = axes.get_legend_handles_labels()
ax_leg.legend(h,legend_labels, loc='center', fontsize=12)
ax_leg.axis('off')
plt.rc('legend', fontsize='50')

fig_leg.savefig('Output_plots/legend.pdf',bbox_inches='tight')

