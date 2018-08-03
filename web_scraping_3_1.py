# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:51:27 2018

@author: rp
"""
# Using Pandas: better for data analysis and working with table data
import pandas as pd
dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0)
for df in dfs:
    print(df)