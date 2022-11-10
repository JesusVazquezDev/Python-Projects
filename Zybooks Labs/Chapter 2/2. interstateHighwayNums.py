#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:26:47 2022

@author: jesusvazquez
"""

highway_number = int(input())

if((highway_number% 100) > 99 or (highway_number % 100) < 1):
    print(highway_number ,"is not a valid interstate highway number.")
else:
    if(highway_number % 2 == 0):
        if(highway_number > 100):
            print(f'I-{highway_number} is auxiliary, serving I-{highway_number % 100}, going east/west.')
        else:
            print(f'I-{highway_number} is primary, going east/west.')
        
    else: 
        if(highway_number > 100):
            print(f'I-{highway_number} is auxiliary, serving I-{highway_number % 100}, going north/south.')
        else:
            print(f'I-{highway_number} is primary, going north/south.')