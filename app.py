#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:32:41 2023

@author: karthick
"""
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")



def lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    
    return r.json()

#Asset
lottie_coding = lottieurl("https://assets5.lottiefiles.com/packages/lf20_4kx2q32n.json")


#---Header Section---
with st.container():
    st.subheader("Hi, I am Karthick :wave:")
    st.title("A Python Developer From India")
    st.write(
            "I am passionate about finding ways to use Python to be more efficient and effective in business settings."
        )
    st.write("[Learn More >](https://gkminds.com/)")
    
    
with st.container():

    st.write("---")    
    left_column,right_column = st.columns(2)
    
    with left_column:
        st.header("Our Services")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."
            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")


#--My Projects--
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
    with image_column:
        #insert imag 
    
    with text_column:
        
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")