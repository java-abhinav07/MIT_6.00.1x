# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 01:26:07 2019

@author: javaa
"""


def bal(balance, annualInterestRate, monthlyPaymentRate):
    """
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    monthlyPaymentRate - minimum monthly payment rate as a decimal 
    
    returns: outstanding balance with 2 decimal digits of accuracy
    """
    month_in = annualInterestRate / 12.0
    
    for month in range(12):
        month_pay = monthlyPaymentRate * balance
        month_unpay = balance - month_pay
        balance = month_unpay + month_in * month_unpay
    
    return round(balance, 2)

print(bal(balance = 42, annualInterestRate = 0.2, monthlyPaymentRate = 0.04))
        
    