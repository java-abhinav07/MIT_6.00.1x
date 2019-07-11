# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 22:52:35 2019

@author: javaa
"""



data = []
file_name = input("Enter file name: ")

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)

else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',') # remove trailing backslash
            data.append(addIt)

finally:
    fh.close() #close file even if fail not a good practice though, hence should be removed

gradesData = []
if data:
    for student in data:
        try:
            name = student[0:-1]
            grades = int(student[-1])
            gradesData.append([[name], [grades]])
        except ValueError:
            gradesData.append([student[:], []])
            
        