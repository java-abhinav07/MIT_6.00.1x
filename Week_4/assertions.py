# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 15:51:17 2019

@author: javaa
"""

def avg(grades):
    assert not len(grades) == 0, "must be a positive length"
    return sum(grades)/len(grades)


print(avg([8,12,2]))
print(avg([]))