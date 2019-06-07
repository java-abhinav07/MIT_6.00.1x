# -*- coding: utf-8 -*-
"""number of vowels in a give string"""
count = 0
s = input("enter string")
l = ['a', 'e', 'i', 'o', 'u']
for letter in s:
    if letter in l: count +=1
print("Number of vowels: {}".format(count))