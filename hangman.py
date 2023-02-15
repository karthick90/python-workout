#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:15:27 20k22

@author: karthick
"""

solution = "joshva".lower()
lives = 10
guess = "_" * len(solution)

# 1. Let the user guess as long as they have lives left
while lives>0 and "_" in guess:
    print("You have " + str(lives) + " lives left...")
    
    # 2. Take the guess from the user
    user_input = input("Guess a character (also whitespace): ").lower()
    
    # 3. Find all indices where the guessed character occurs in the solution
    indices = []
    for i in range(len(solution)):
        if solution[i]==user_input:
            indices += [i]
    
    # 4. Test whether the guessed character didn't occur -- reduce lives if so
    if len(indices)==0:
        lives = lives - 1
    
    # 5. Fill in the guess at all correct indices
    for index in indices:
        guess = guess[:index] + user_input + guess[index+1:]
    
    # 6. Output current (partial) solutions
    print("The secret phrase:")
    output = ""
    for c in guess:
        output += c + " "
    print(output)
    print("")

# 7. Successfull termination?   
if lives==0:
    print("Game over!")
else:
    print("You won!")