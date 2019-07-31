# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:37:37 2019

@author: javaa
"""

# merge sort
def merger(l1, l2, l):
    i = 0
    j = 0
    k = 0
    while i < len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            l[k] = (l2[j])
            j += 1
            k += 1
        elif l1[i] < l2[j]:
            l[k] = (l1[i])
            i += 1
            k += 1
    while i < len(l1):
        l[k] = (l1[i])
        i += 1
        k += 1
    while j < len(l2):
        l[k] = (l2[j])
        j += 1 
        k += 1

def sort(l):
    mid = len(l) // 2
    if len(l) == 0 or len(l) == 1:
        return l
    l1 = l[:mid]
    l2 = l[mid:]
    sort(l1)
    sort(l2)
    merger(l1, l2, l)
    