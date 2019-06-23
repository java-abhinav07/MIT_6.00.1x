# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:17:00 2019

@author: javaa
"""
# general method to find roots of a polunomial

epsilon = 0.01
y = 2400.0
guess = y/2.0
num = 0

while abs(guess*guess - y)>=epsilon:
    num += 1
    guess -= (((guess**2) - y)/(2*guess))

print('num of guesses = ' + str(num))
print('Square root of ' + str(y) + ' is about ' + str(guess))
