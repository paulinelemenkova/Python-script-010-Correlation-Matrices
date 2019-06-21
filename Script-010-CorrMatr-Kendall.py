#!/usr/bin/env python
# coding: utf-8
import os
import numpy as np
import pandas as pd
import matplotlib.pylab as pylab
from matplotlib import pyplot as plt
import seaborn as sb

os.chdir('/Users/pauline/Documents/Python')
sb.set(style='white')
sb.set_context('paper')

params = {'figure.figsize': (10, 10),
        'legend.fontsize': 14,
        'font.family': 'Times'
        }
pylab.rcParams.update(params)

df = pd.read_csv("Tab-Morph.csv")
corr = df.corr(method='kendall')
cmap="RdYlBu"

# plotting heatmap
f, ax = plt.subplots()
sb.heatmap(corr, cmap=cmap, center=0,
           vmin=-1.1, vmax=1.1,
           annot=True, annot_kws={"size":8},
           square=True, linewidths=.05, linecolor='grey',
           cbar=True, mask=False, cbar_kws={"shrink": .5},
           )
plt.title('Mariana Trench: Kendall correlation for the environmental factors',
          fontsize=13, fontfamily='serif')
plt.subplots_adjust(bottom=0.15,top=0.85, right=0.90, left=0.10)
plt.xticks(rotation=30)
plt.yticks()

# visualizing and saving figure
plt.tight_layout()
plt.savefig('plot_CorrK.png', dpi=300)
plt.show()
