#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:28:44 2022

@author: jesusvazquez
"""

par = int(input())
score = int(input())

if(par > 5 or par < 3):
    print("Error")
    exit()

if(par != score):
    if(par == (score + 2)):
        print("Eagle")
    elif(par == (score + 1)):
        print("Birdie")
    else:
        print("Bogey")
else:
    print("Par")