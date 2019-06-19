#!/usr/bin/env python
# coding: utf-8
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

os.chdir('/Users/pauline/Documents/Python')
sb.set(style='white')
sb.set_context('paper')

df = pd.read_csv("Tab-Morph.csv")

# compute correlation matrix
corr = df.corr(method='kendall')

# generate a custom diverging colormap
cmap="RdYlBu"

# plotting heatmap
f, ax = plt.subplots(figsize=(11, 9))
sb.heatmap(corr, cmap=cmap, center=0,
           vmin=-1.1, vmax=1.1,
           annot=True, annot_kws={"size":8},
           square=True, linewidths=.05, linecolor='grey',
           cbar=True, mask=False, cbar_kws={"shrink": .5},
           )
plt.title('Mariana Trench: Kendall correlation for the environmental factors',
          fontsize=13, fontfamily='serif')
plt.subplots_adjust(bottom=0.15,top=0.85, right=0.90, left=0.10)
plt.xticks(rotation=30, size=9)
plt.yticks(rotation=0, size=9)

# visualizing and saving figure
plt.tight_layout()
plt.savefig('plot_CorrK.png', dpi=300)
plt.show()
