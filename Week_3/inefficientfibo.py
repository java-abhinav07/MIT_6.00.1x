# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 00:08:29 2019

@author: javaa
"""

def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
numFibCalls = 0
fibArg = 20

print(fib(fibArg))
print('function calls', numFibCalls)