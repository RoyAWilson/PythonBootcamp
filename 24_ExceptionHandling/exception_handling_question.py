#!/usr/bin/env python
# coding: utf-8

# # Exception Handling Question
#
# Write a few lines of code that will open and read text file line by line to a variable. Use a try and except block to handle the event of the file not existing.

# In[ ]:
import csv
try:
    f = csv.reader(open(r'./my_csv.csv'))
except FileNotFoundError as err:
    print('I cannot find that file or directory.  Please check that it exists.')
    print(
        f'If problem continues please report quoting the error message: {err}')
