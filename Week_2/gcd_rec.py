# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:20:34 2019

@author: javaa
"""

def gcd(a, b):
    x = min(a, b)
    y = max(a, b)
    if x == 0:
        return y
    else:
        return gcd(x, y%x)
    
print(gcd(12, 112))
    