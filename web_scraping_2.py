# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:37:00 2018

@author: rp
"""

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')

# get the links from the nav bar
# =============================================================================
# nav = soup.nav
# for url in nav.find_all('a'):
#     print(url.get('href'))
# =============================================================================
    
# find all text from paragraph tags in the body section
# =============================================================================
# body = soup.body
# for paragraph in body.find_all('p'):
#     print(paragraph.text)
# =============================================================================

# get specific tag and class
for div in soup.find_all('div', class_='body'):
    print(div.text)
