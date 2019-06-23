# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:34:19 2019

@author: javaa
"""

balance = 320000
annualInterestRate = 0.2
epsilon = 0.01
hi = (balance*(1+annualInterestRate/12.0)**12.0)/12.0
low = balance/12.0
ans = (hi + low)/2.0
while True:
    temp = balance
    for i in range(12):
        temp -= ans
        temp *= (1+annualInterestRate/12)
    print(temp)
    if abs(temp) <= epsilon:
        break
    elif temp < 0:
        hi = ans
    elif temp > 0:
         low = ans
    ans = (hi + low)/2.0
        
print('Lowest Payment: ' + str(ans))