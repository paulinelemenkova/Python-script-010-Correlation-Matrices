#!/usr/bin/env python
# coding: utf-8
#
from string import ascii_letters
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
corr = df.corr(method='spearman')
#
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))
#
# Colormap
pal = sb.color_palette("RdGy_r")
cmap=pal
#
# Draw the heatmap with the mask and correct aspect ratio
sb.heatmap(corr, cmap=cmap, robust=False,
           vmin=-1.1, vmax=1.1, center=0,
           annot=True, annot_kws={"size":8},
           square=True, linewidths=.05, linecolor='grey', 
           cbar=True, mask=False, cbar_kws={"shrink": .5}, )
plt.title('Mariana Trench: Spearman correlation for the environmental factors',
          fontsize=13, fontfamily='serif')
plt.subplots_adjust(bottom=0.20,top=0.90, right=0.90, left=0.10)
plt.xticks(rotation=30, size=9) 
plt.yticks(rotation=0, size=9)
plt.show()
