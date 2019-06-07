# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:52:34 2019

@author: javaa
"""
s = 'boboboboboobdjvnejroovvoirgiovnobobboboobbobobkjv'
count = 0 
for i in range(0, len(s) - 2, 1):
    if s[i:i+3] == 'bob': 
        count += 1
print("Number of times bob occurs is:{}".format(count))