#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 09:59:50 2022

@author: karthick
"""
#import required library
import requests
from bs4 import BeautifulSoup

#create user agent
headers ={ "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}



#get request
response = requests.get("https://kinsta.com/", headers = headers )

#Check status code
#print(response.status_code)

#save webpage content
webpage = response.content

# create soup object
soup = BeautifulSoup(webpage,"html.parser")

#print(soup.prettify())

#Accessing tags via tag name
#head_tag=soup.head
#print(head_tag)
#print(soup.head.contents[3])


#using child name generator
'''for child in soup.head.descendants:
    if child!= "\n":
        print(child)
        
children=[child for child in soup.head.children if child!="\n"]
print(children)
print(len(children))


descendent=[x for x in soup.head.descendants if x!="\n"]
print(descendent)
print(len(descendent))'''


#find the parent
#print(soup.title.parent.name)

#find sibings

 



    
'''for x in soup.p.previous_siblings:
    print(x)'''
    
    
#print(soup.title.string)

'''for c in soup.body.stripped_strings:
    print(c)'''
#print(soup.find_all('p')[1]) 
#print(len(soup.find_all('p')) )
print(soup.find_all('div')[1] )
print(len(soup.find_all('div')) )




        
