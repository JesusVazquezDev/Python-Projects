#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:42:10 2022

@author: jesusvazquez
"""

names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())

#  Use a try block to output the name and an except block to catch any IndexError.
# Type your code here.

try:
    print(f'Name: {names[index]}')
except IndexError:
    print(f'Exception! list index out of range')
    if(index < 0):
        print(f'The closest name is: {names[0]}')
    else:
        print(f'The closest name is: {names[-1]}')