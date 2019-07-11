# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:27:42 2019

@author: javaa
"""

try:
    a = int(input("tell me one number: "))
    b = int(input("tell me one number: "))
    print(a/b)
    print("okaie")
except ValueError:
    print("couldnt convert to number")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("fix bug")


print("outside")
    

