# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:46:31 2018

@author: rp
"""

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

table = soup.find('table')
# table = soup.table #works because page only has 1 table

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)