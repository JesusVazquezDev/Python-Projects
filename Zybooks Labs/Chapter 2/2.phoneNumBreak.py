#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:29:03 2022

@author: jesusvazquez
"""

phone_number = int(input())
# First 3 digits
firstThree = phone_number // 10000000

middleThree = (phone_number // 10000) - (firstThree * 1000)


# Last 4 digits 
lastFour = phone_number % 10000

print(f'({firstThree}) {middleThree}-{lastFour}')

