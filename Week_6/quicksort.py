# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:13:11 2019

@author: javaa
"""

def quicksort(arr, start, end):
    if end - start <= 0:
        return
    partindex = partition(arr, start, end)
    quicksort(arr, start, partindex-1)
    quicksort(arr, partindex+1, end)

def partition(arr, start, end):
    target = arr[start]
    count = 0
    
    for l in range(start, end):
        if arr[l] < target:
            count += 1
    arr[start], arr[start+count] = arr[start+count], arr[start]
    i = start
    j = end
    
    while i < j:
        if arr[i] < target:
            i += 1
        elif arr[j] >= target:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
    return (start + count)