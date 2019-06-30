# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:24:12 2019

@author: javaa
"""

# fibonacci with a dict

def fib_efficient(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
d = {1:1, 2:2}

numFibCalls = 0
fibArg = 20
print(fib_efficient(fibArg, d))
print('function calls', numFibCalls)
numFibCalls = 0