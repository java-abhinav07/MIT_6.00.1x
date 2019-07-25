# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:08:18 2019

@author: javaa
"""


def genFib():
    fib_1 = 1
    fib_2 = 0
    while True:
        next = fib_1 + fib_2
        yield next
        fib_2 = fib_1
        fib_1 = next
        