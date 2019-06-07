# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:49:51 2019

@author: javaa
"""

import re
regexvowel = re.compile(r'[AEIUOaeiou]')
print(len(regexvowel.findall('This is a string')))
