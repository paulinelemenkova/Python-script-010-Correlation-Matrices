#!/usr/bin/env python
# coding: utf-8
#
import numpy as np
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
import os
#
os.chdir('/Users/pauline/Documents/Python')
sb.set(style="white")
df = pd.read_csv("Tab-Morph.csv")
#
# Compute correlation matrix
corr = df.corr(method='kendall')
#
# Set up matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))
#
# Generate a custom diverging colormap
cmap="RdYlBu"
#
# Draw heatmap with mask and correct aspect ratio
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
plt.show()
