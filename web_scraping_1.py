# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:08:59 2018

@author: rp
"""

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')

# =============================================================================
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# =============================================================================

# =============================================================================
# for paragraph in soup.find_all('p'):
#     print(paragraph.string)
#     print(str(paragraph.text))
# =============================================================================
    
# =============================================================================
# for url in soup.find_all('a'):
#     print(url.get('href'))
# =============================================================================
print(soup.get_text())
