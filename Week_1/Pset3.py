# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:53:33 2019

@author: javaa
"""

"""Write a program that prints the longest substring of 
s in which the letters occur in alphabetical order. For 
example, if s = 'azcbobobegghakl', then your program should print- 
Longest substring in alphabetical order is: beggh"""

s = 'pohizzcdhgtlqf'

res_str = ""
result = []
temp = []
for i in range(1, len(s)):
    if ord(s[i-1]) <= ord(s[i]):
        if len(res_str) != 0:
            res_str += s[i]
        else: res_str += s[i-1] + s[i]
    else:
        result.append(res_str)
        temp.append(len(res_str))
        res_str = ""

result.append(res_str)
temp.append(len(res_str))
result[:] = (value for value in result if value != "")
temp[:] = (val for val in temp if val != 0)
print(result)
print(temp)
if temp:
    ma = temp.index(max(temp))
    print("Longest substring in alphabetical order is: {}".format(result[ma]))
else: print("Longest substring in alphabetical order is: {}".format(s[0]))
            
        
    