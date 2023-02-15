#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 11:18:53 2022

@author: karthick
"""

import requests
from bs4 import BeautifulSoup

#Add user agent
headers ={ "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

response=requests.get("https://app.finxter.com/learn/computer/science/", headers=headers)

webpage=response.content 

soup=BeautifulSoup(webpage,"html.parser")

#print(response.status_code)
#print(webpage)


for table in soup.find_all('table',class_='w3-table-all', limit=1):
    for tr in table.find_all('tr'):
        name='Username: '
        elo='Elo: '
        rank='Rank: '
        for td in tr.find_all('td'):
            
            print(name,td.text.strip())
            name = elo
            elo = rank
        print()
    