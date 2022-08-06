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

# Basal --> Treg(1), Th2(1), Th17(1), Th1(1) --> ../Output/basal.txt 
# Mild --> Treg(0), Th2(1), Th17(0.5), Th1(0) --> ../Output/sim_1_tmp_0.txt 
# Medial --> Treg(0), Th2(0.5), Th17(1), Th1(0) --> ../Output/sim_tmp_1_0.txt 
# Moderate --> Treg(0), Th2(0.5), Th17(1), Th1(1) --> ../Output/sim_tmp_1_1.txt 
title = 'MILD (Row 7)'
fname = '../All_panels/7.mild_1_1_0.pdf'

df = pd.read_csv("../Output/sim_1_1_0.txt",sep ='\t')
df = df.T

# print(df.shape, df.head())


df_dict = {}
for name in df.columns:
    row = np.mean(np.array(df[name]).reshape(runs,cycles), axis = 0)
    df_dict[name] = row


data = pd.DataFrame(df_dict)

columns  = ['Treg','Stimulant_I', 'Stimulant_II', 'Stimulant_III',
        'DC1', 'DC2', 'DC3',
       'IL4', 'IL6', 'IL12', 
       'Th0', 'Th2', 'Th17', 'Th1', 
        'Th9','IL9', 'IL13', 'B_Cells', 'IgE', 'Mast_Cells', 'IL5', 'IL3',
        'Leukotrine', 'Histamine', 'PGD2',  'Epithelial_Cells', 'Eotaxin',  
         'TGF_beta', 'IL21', 'IFN_gamma', 'Mphi','M1', 'M2', 'IL2',
       'Tc0',  'Tc', 'IL17', 'TNF_alpha', 'IL8',
      'Basophils',
       'Eosinophils', 'Neutrophils' ]

data_sub = data[columns]

x_ticks = np.arange(0, 801, 100)
y_ticks = np.arange(0, 1.1, 0.5)
axes = data_sub.plot(subplots=True, layout=(7,6), figsize=(12, 10), 
  ylim=[-0.03,1.03], xlim=[-1,801],   yticks = y_ticks, color='hotpink', lw=2, 
  legend=False)#, title='BASAL')
fig=axes[0,0].figure
fig.text(0.5,0, "Time Steps", ha="center", va="center", fontsize = 16)#, weight = 'bold')
fig.text(0,0.5, "Node Activity", ha="center", va="center", rotation=90, fontsize=16)#, weight ='bold')



columns  = ['T$-$reg', 'Stimulant T$_\mathrm{H}$2', 'Stimulant T$_\mathrm{H}$17', 'Stimulant T$_\mathrm{H}$1',
        'DC1', 'DC2', 'DC3', 
        'IL$-$4', 'IL$-$6', 'IL$-$12',
         'T$_\mathrm{H}$0','T$_\mathrm{H}$2', 'T$_\mathrm{H}$17', 'T$_\mathrm{H}$1',
        'T$_\mathrm{H}$9','IL$-$9', 'IL$-$13', 'B Cells', 'IgE', 'Mast Cells', 'IL$-$5', 'IL$-$3', 
       'Leukotrienes','Histamines', 'PGD2', 'Epithelial Cells', 'Eotaxin', 
        r'TGF$\beta$', 'IL$-$21', r'IFN$\gamma$', r'M$\phi$', 'M1', 'M2', 'IL$-$2',
      'T$_\mathrm{c}$0', 'T$_\mathrm{c}$', 'IL$-$17', r'TNF$\alpha$','IL$-$8',
       'Basophils', 
        'Eosinophils', 'Neutrophils']  


k=0
for i in range(7):
    for j in range(6):
        # if k <= 40:
          print(i, j, k, columns[k])
          axes[i,j].set_title(columns[k], fontsize = 15)
          axes[i,j].set_xticks(x_ticks)
          axes[i,j].set_xticklabels(x_ticks,rotation=60, fontsize=8)
          axes[i,j].set_yticklabels(y_ticks,rotation=0, fontsize=8)
          k+=1

# print(plt.style.available)
plt.suptitle(title, fontsize=24,y=1.03)
plt.tight_layout()
plt.savefig(fname,bbox_inches='tight')

