# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 16:47:58 2019

@author: javaa
"""

cube = 29
epsilon = 0.01
guess = 0.0
increment = 0.01
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print(num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print("failed cube root of", cube)
else:
    print(guess, 'is close to the cube root of', cube)