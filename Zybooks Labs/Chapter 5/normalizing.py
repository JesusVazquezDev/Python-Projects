#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:38:37 2022

@author: jesusvazquez
"""

# Gives us the count
count = int(input())

i = 0 

# Populate list 
values = []
for i in range(count):
   values.append(float(input()))

maxValue = max(values)

for i in values:
    print(f'{i / maxValue:.2f}')

