#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 20:22:30 2022

@author: karthick
"""
import random
get_num=input("Enter a number = ")
if get_num.isdigit():
    get_num=int(get_num)
    if get_num <= 0:
        print("Please enter larger than zero")
        quit()
else:
    print("Enter a valid integer")
    quit()

random_number=random.randint(0, get_num)  
guess_count = 0  
#print(random_number)
while True:
    guess_count += 1
    user_guess=input("Guess the Number = ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
        if user_guess <= 0:
            print("Enter the number larger than 0 ")
        
    else:
        print("Enter a valid integer ")
        quit()
    
    if user_guess == random_number:
        print("You got the number!")
        break
        
    else:
        print("You Missed it")
        if user_guess<random_number:
            print("please enter above from ur gessing")
        else:
            print("please enter below from your guessing")
        continue

print("You take ",guess_count,"guess")
    

