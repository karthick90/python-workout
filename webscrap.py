#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 22:49:04 2022

@author: karthick
"""

import requests


response = requests.get("https://www.amazon.co.uk/2nd-generation-wireless-cancellation-charging-PowerWave/dp/B094Q58PR4/ref=sr_1_1?keywords=echo+buds&qid=1671768845&sprefix=echo+buds%2Caps%2C304&sr=8-1")
webpage = response.content
#print(webpage)
'''headinfo = response.headers

for key,value in headinfo.items():
    print(key, ' = ', value)'''
    
print(response.request.headers)
    
print(response.status_code)