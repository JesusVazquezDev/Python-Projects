#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:26:18 2022

@author: jesusvazquez
"""

red = int(input())
green = int(input())
blue = int(input ())

if(red < green and red < blue):
    green -= red
    blue -= red
    red -= red
    print(red , green , blue)
    
elif(green < red and green < blue):
    red -= green
    blue -= green
    green -= green   
    print(red , green , blue)
    
elif(blue < green and blue < red):
    red -= blue
    green -= blue
    blue -= blue
    print(red , green , blue)
else:
    red -= blue
    green -= blue
    blue -= blue
    print(red , green , blue)
    