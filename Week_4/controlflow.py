# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:21:09 2019

@author: javaa
"""

def get_ratios(L1, L2):
    """Assumes L1 and L2 are lists of equal length of numbers 
    returns: a list containing l1/l2 """

    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index])/float(L2[index])
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('get_ratios called with bad arguments')
        return ratios
    