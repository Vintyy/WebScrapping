# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:29:58 2019

@author: vineeth.vijay.das
"""

import re
import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('https://timesofindia.indiatimes.com/2010/1/1/archivelist/year-2010,month-1,starttime-40179.cms')
soup = BeautifulSoup(html)
data = soup.findAll(text=True)

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

result = filter(visible, data)

print (result)
#print list(result)