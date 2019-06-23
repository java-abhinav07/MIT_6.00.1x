# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:12:12 2019

@author: javaa
"""

def gcd(n, m):
    x = max(n, m)
    y = min (n, m)
    for i in range(y, 0, -1):
        if x % i == 0 and y % i == 0:
            return i
        

print(gcd(99,12))