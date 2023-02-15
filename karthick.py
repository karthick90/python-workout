#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:22:01 2022

@author: karthick
"""

solution='karthick'.lower()
lives=2
#print(len(solution))
guess="_"* len(solution)

#print(guess)
while lives>0 and "_" in guess:
    print("you have "+ str(lives)+" Remaining")
    #print(guess)
#   lives-=1
#Get input from user
    user_input=input("Guess the Character: ").lower()

#Check with Solution
    indices = []
    for i in range(len(solution)):
        if solution[i]==user_input:
            indices += [i]
    if len(indices)==0:
        lives-=1
            
    for k in indices:
        guess=guess[:k] + user_input + guess[k+1:]
    
    print("The secret phrase:")
    output = ""
    for c in guess:
        output += c + " "
    print(output)
    print("")
            
            
            


#Final
if lives==0:
    print("Game Over")
else:
    print("You Won")