#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:28:19 2022

@author: jesusvazquez
"""

is_leap_year = False
   
input_year = int(input())

if(input_year % 4 == 0):
    if((input_year - input_year % 100) % 400 == 0):
        print(f'{input_year} - leap year')
    else:
        print(f'{input_year} - not a leap year')
else:
    print(f'{input_year} - not a leap year')
