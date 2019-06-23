# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:52:46 2019

@author: javaa

"""
balance = 3926
annualInterestRate = 0.2
def min_rate(bal, air, mina):
    """
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    monthlyPaymentRate - minimum monthly payment rate as a decimal
    
    returns:  minimum monthly payment required by the credit card company 
                each month such that debt is paid of in 12 months.
    """
    temp = bal
    for i in range(12):
            temp = (temp-mina)
            temp *= (1+air/12)
    if temp > 0:
        return min_rate(bal, air, mina+10)
    else:
        return mina

print('Lowest Payment: ' + str(min_rate(balance, annualInterestRate, 10)))
