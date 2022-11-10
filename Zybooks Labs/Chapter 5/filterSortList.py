#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:37:07 2022

@author: jesusvazquez
"""

testing = input()
testing = testing.split()

testing = list(map(int, testing))

finalList = []

for i in testing:
    if i >= 0:
        finalList.append(i)
       
finalList.sort() 

for i in finalList:
    print(f'{i}', end =' ')
