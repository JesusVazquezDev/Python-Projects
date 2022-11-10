#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:24:29 2022

@author: jesusvazquez
"""

x = int(input())
y = int(input())
z = int(input())

if x < y and x < z:
    print(x)
    
if y < z and y < x:
    print(y)
    
else:
    print(z)