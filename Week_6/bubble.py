# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:20:35 2019

@author: javaa
"""

def bubblesort(l):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                sorted = False
    return l


        
    
        