# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:25:35 2019

@author: javaa
"""
import math
def polysum(n, s):
    """
    Takes 2 arguments, 'n' and 's'. This function sums the area and 
    square of the perimeter of the regular polygon. 
    The function returns the sum, rounded to 4 decimal places.
    """
    # mathematical expression for area
    area = (n*s*s)/((math.tan(math.pi/n))*4)
    # mathematical expression for square of perimeter
    perisq = (s*n)**2
    # rounding off the sum
    rsum = round(area+perisq, 4)
    return rsum

    
    
    