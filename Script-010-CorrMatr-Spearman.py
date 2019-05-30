#!/usr/bin/env python
# coding: utf-8

# In[18]:


from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
import os
os.chdir('/Users/pauline/Documents/Python')
sb.set(style="white")

df = pd.read_csv("Tab-Morph.csv")

# Compute the correlation matrix
corr = df.corr(method='spearman')
# Generate a mask for the upper triangle
#mask = np.zeros_like(corr, dtype=np.bool)
#mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
#cmap = sb.diverging_palette(150, 275, s=80, l=55, n=9)
#cmap=sb.color_palette("cubehelix", 8)
#pal = sb.dark_palette("palegreen", as_cmap=True)
#pal = sb.color("Blues", reverse=True)
pal = sb.color_palette("RdGy_r")
cmap=pal
#cmap="cubehelix

# Draw the heatmap with the mask and correct aspect ratio
sb.heatmap(corr, cmap=cmap, robust=False,
           vmin=-1.1, vmax=1.1, center=0,
           annot=True, annot_kws={"size":8},
           square=True, linewidths=.05, linecolor='grey', 
           cbar=True, mask=False, cbar_kws={"shrink": .5}, )
plt.title('Mariana Trench: Spearman correlation for the environmental factors', fontsize=13, fontfamily='serif')
plt.subplots_adjust(bottom=0.20,top=0.90, right=0.90, left=0.10)
plt.xticks(rotation=30, size=9) 
plt.yticks(rotation=0, size=9)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




