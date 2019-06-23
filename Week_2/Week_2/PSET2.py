# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 01:26:07 2019

@author: javaa
"""


def min_rate(bal, air):
    """
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    monthlyPaymentRate - minimum monthly payment rate as a decimal
    
    returns:  minimum monthly payment required by the credit card company 
                each month such that debt is paid of in 12 months.
    """
    min_a = 10.0
    while True:
        temp = bal
        for i in range(12):
            temp = temp - min_a
            temp = temp*(1 + air/12)
        if temp <= 0:
            break
        else:
            min_a = min_a + 10
            
    return min_a
            
print(min_rate(3329, 0.2))       
    
