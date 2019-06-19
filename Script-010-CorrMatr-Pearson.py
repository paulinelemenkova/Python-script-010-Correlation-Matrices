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

# computing correlation matrix
corr = df.corr(method='pearson')

# generating colormap
pal = sb.color_palette("tab20c")
cmap=pal

# plotting heatmap
f, ax = plt.subplots(figsize=(11, 9))
sb.heatmap(corr, cmap=cmap, vmax=0.3, center=0, annot=True,
           annot_kws={"size":8}, square=True, linewidths=.05, linecolor='grey',
           cbar=True, mask=False, cbar_kws={"shrink": .5}
           )
plt.title('Mariana Trench: Pearson correlation for the environmental factors',
          fontsize=13, fontfamily='serif')
plt.subplots_adjust(bottom=0.20, top=0.90, right=0.90, left=0.10)
plt.xticks(rotation=30, size=9)
plt.yticks(rotation=0, size=9)

# visualizing and saving
plt.tight_layout()
plt.savefig('plot_CorrP.png', dpi=300)
plt.show()
