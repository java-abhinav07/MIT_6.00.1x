# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:15:25 2019

@author: javaa
"""

def genPrimes():
    p, primes = 2, []
    while True:
        if all(p%nex for nex in primes):
            yield p
            primes.append(p)
        p += 1
        

    