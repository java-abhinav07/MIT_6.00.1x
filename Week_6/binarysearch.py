# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:13:50 2019

@author: javaa
"""

# binary search
def binsearch(arr, h, l, k):
    if l == h:
        return -1
    mid = (h + l + 1) // 2
    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        h = mid
    elif arr[mid] < k:
        l = mid
    return binsearch(arr, h, l, k)