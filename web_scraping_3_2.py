# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:52:51 2018

@author: rp
"""
# Parse XML on the sitemap
import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(source,'xml')

for url in soup.find_all('loc'):
    print(url.text)