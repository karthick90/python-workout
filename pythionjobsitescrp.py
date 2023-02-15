#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 11:54:43 2022

@author: karthick
"""

import requests
from bs4 import BeautifulSoup

headers ={ "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

response = requests.get("https://pythonjobs.github.io/", headers=headers)
webpage = response.content
#print(response.status_code)
soup = BeautifulSoup(webpage,"html.parser")

for job in soup.find_all('section', class_='job_list'):
    #for title in div.find_all('h1'):
       # print(title.text)
    title=[a for a in job.find_all('h1')]
    for n,tag in enumerate(job.find_all('div', class_='job')):
        company_element=[x for x in tag.find_all('span', class_='info')]
        print('Title: ',title[n].text.strip())
        print('Location: ',company_element[0].text.strip())
        print('Company: ', company_element[3].text.strip())
        print()
    
        