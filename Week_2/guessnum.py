# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 00:47:23 2019

@author: javaa
"""


print("Please think of a number between 0 and 100!")
h = 100
l = 0
while True:
    guess = (l + h) // 2
    print("Is your secret number {}?".format(guess))
    token = input("Enter 'h' to indicate the guess is too high.\
          Enter 'l' to indicate the guess is too low.\
          Enter 'c' to indicate I guessed correctly. ")
    if token == 'c':
        break
    elif token == 'h':
        h = guess
    elif token =='l':
        l = guess
    else:
        print("Sorry, I did not understand your input.")
        token = input("Enter 'h' to indicate the guess is too high.\
          Enter 'l' to indicate the guess is too low.\
          Enter 'c' to indicate I guessed correctly")
        

print("Game over. Your secret number was: {}".format(guess))


        
        
    


