#plot the simulations
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from pylab import *
import matplotlib as mpl
import seaborn as sns
import pandas as pd


runs = 350 #numseries
cycles = 800  #nummeasurements


df = pd.read_csv("../Output/overlap1.txt",sep ='\t')
df = df.T


df_dict = {}
print(df.columns)
for name in df.columns:
    row = np.mean(np.array(df[name]).reshape(runs,cycles), axis = 0)
    df_dict[name] = row


data = pd.DataFrame(df_dict)
df = data


## Plot heatmap
fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 2]}, figsize=(6,4))
ax1 = ax[0]
ax2 = ax[1]
#plt.suptitle('Overlap',  y=0.95, fontsize=16,weight="bold")
df2 = data[['Eosinophils', 'Neutrophils']]#,'IgE', 'IL6','IL9','IL12']]
df1 = data[['Th2', 'Th17', 'Th1']]
yticklabels = ['T$_\mathrm{H}$2', 'T$_\mathrm{H}$17', 'T$_\mathrm{H}$1']
sns.heatmap(df1.T[df1.T.columns[::100]], vmin=0, vmax=1, cmap='RdYlGn', linewidths=.5, cbar=False, xticklabels=np.arange(50,850,100),ax=ax1, yticklabels=yticklabels)  #cmap='PiYG','BrBG','PuOr'
sns.heatmap(df2.T[df2.T.columns[::100]], vmin=0, vmax=1, cmap='RdYlGn', linewidths=.5, cbar=False, xticklabels=np.arange(50,850,100),ax=ax2)

ax = fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
ax1.tick_params(axis='both',  labelsize=16, rotation = 0,bottom=False)
ax1.set_xticklabels('')

plt.yticks(rotation=0)
ax2.tick_params(axis='both',  labelsize=16, rotation = 0)
plt.xticks(fontweight = 'bold')
plt.xlabel('Time Steps',fontsize=20,fontweight='bold')
plt.ylabel('Node Activity', fontsize=20,fontweight='bold')
ax.get_yaxis().set_label_coords(-0.30,0.5)
ax.get_xaxis().set_label_coords(0.5,-0.1)
#plt.tight_layout()
plt.savefig('Overlap1.pdf',bbox_inches='tight')


## Plot Colorbar
#cmap = 'BrBG'
#cmap = 'PiYG'
cmap = 'RdYlGn'

import matplotlib.pyplot as plt
import numpy as np

cmap = plt.cm.get_cmap(cmap)
colors = cmap(np.arange(cmap.N))

fig, ax = plt.subplots(1, figsize=(6, 2),
                           subplot_kw=dict(xticks=[], yticks=[]))
ax.set(frame_on=False)

ax.imshow([colors], extent=[0, 10, 2, 0.5])
xmarks = [0,5,10]
ax.set_xticks(xmarks)
ax.set_xticklabels(['INACTIVE', 'LOW', 'HIGH'], fontsize=18, fontweight='bold')


plt.savefig('cbar.pdf',bbox_inches='tight')



