# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:56:25 2018

@author: rp
"""
# Scraping Dynamic Data/js text
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebPage
import bs4 as bs
import urllib.request

class Client (QWebPage):
    
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
        
       #want the page to load 
    def on_page_load(self):
        self.app.quit()
        
url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()

soup = bs.BeautifulSoup(source,'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)