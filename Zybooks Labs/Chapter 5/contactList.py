#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:38:16 2022

@author: jesusvazquez
"""

contacts = input()

saved = contacts.split(' ')

mult_table = [[str(num) for num in line.split(',')] for line in saved]

find = input()

for i in mult_table:
    if i[0] == find:
        print(i[1])