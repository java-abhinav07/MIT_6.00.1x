# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:03:27 2019

@author: javaa
"""

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to ,spare)
        Towers(n-1, spare, to, fr)
        

print(Towers(5, "P1", "P2", "P3"))
