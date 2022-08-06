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
 
df = pd.read_csv("../Output/overlap3.txt",sep ='\t')
df = df.T

print(df.shape, df.head())


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
      'Basophils',   'Eosinophils',  'Neutrophils' ]

data_sub = data[columns]


yticklabels  = ['T$-$reg', 'Stimulant T$_\mathrm{H}$2', 'Stimulant T$_\mathrm{H}$17', 'Stimulant T$_\mathrm{H}$1',
        'DC1', 'DC2', 'DC3', 
        'IL$-$4', 'IL$-$6', 'IL$-$12',
         'T$_\mathrm{H}$0','T$_\mathrm{H}$2', 'T$_\mathrm{H}$17', 'T$_\mathrm{H}$1',
       'T$_\mathrm{H}$9', 'IL$-$9', 'IL$-$13', 'B Cells', 'IgE', 'Mast Cells', 'IL$-$5', 'IL$-$3', 
       'Leukotrienes','Histamines', 'PGD2', 'Epithelial Cells', 'Eotaxin', 
        r'TGF$\beta$', 'IL$-$21', r'IFN$\gamma$', r'M$\phi$', 'M1', 'M2', 'IL$-$2',
      'T$_\mathrm{c}$0', 'T$_\mathrm{c}$', 'IL$-$17', r'TNF$\alpha$','IL$-$8',
       'Basophils',  'Eosinophils', 'Neutrophils' ]  


plt.figure(figsize = (10,20))
sns.set(font_scale=2.1)
heatmap = sns.heatmap(data_sub.T[data_sub.T.columns[::50]], vmin=0, vmax=1, cmap='RdYlGn', 
  linewidths=.5, cbar=False, 
  #xticklabels=np.arange(50,850,50),
  yticklabels=yticklabels)


heatmap.set_xticklabels(np.arange(50,850,50),rotation=90)
#heatmap.set_yticklabels(yticklabels,rotation=0, fontsize=20)
#heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=30) 


plt.tight_layout()
plt.savefig('heatmap_overlap3.pdf',bbox_inches='tight')



