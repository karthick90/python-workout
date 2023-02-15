#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 18:06:00 2022

@author: karthick
"""

import requests
from bs4 import BeautifulSoup

#create user agent
headers ={ "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
#get request
response = requests.get("https://www.amazon.in/b/?node=1318160031&ref_=Oct_d_odnav_d_1318157031_0&pd_rd_w=Gg80Z&content-id=amzn1.sym.8fe3259a-5917-4cb4-a137-2310adc9c0ad&pf_rd_p=8fe3259a-5917-4cb4-a137-2310adc9c0ad&pf_rd_r=BMJ76GMDC0DH72TMH9R2&pd_rd_wg=L27UB&pd_rd_r=7da663fe-3254-4306-b075-adad7285c7a1", headers = headers )
webpage = response.content
#print(response.status_code)
soup  = BeautifulSoup(webpage,"html.parser")


for parent in soup.find_all('div',class_ ="octopus-pc-asin-title"):
    #for n,tag in enumerate(parent.find_all('span')):
      #  title=[x for x in tag.find_all('span',class_="a-size-base a-color-base")]
       # print(title)
     print(parent)