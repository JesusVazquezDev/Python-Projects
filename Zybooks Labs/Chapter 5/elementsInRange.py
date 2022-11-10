#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:37:45 2022

@author: jesusvazquez
"""

userInput = input()
final = list(map(int,userInput.split()))

sec = input()
bounds = list(map(int,sec.split()))

for i in final:
    if i <= bounds[1] and i >= bounds[0]:
        print(f'{i}', end=' ')

