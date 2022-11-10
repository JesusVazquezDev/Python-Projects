#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:27:55 2022

@author: jesusvazquez
"""

currency = int(input())

if(currency == 0):
    print("No change")
    exit()

dollars = currency// 100
currency -= 100 * dollars

quarters = currency// 25
currency -= 25 * quarters

dimes = currency // 10
currency -= 10 * dimes

nickels = currency // 5
currency -= 5 * nickels

pennies = currency // 1
currency -= 1 * pennies

if(dollars == 1):
    print(f'{dollars} Dollar')
if(dollars > 1):
    print(f'{dollars} Dollars')

if(quarters == 1):
    print(f'{quarters} Quarter')
if(quarters > 1):
    print(f'{quarters} Quarters')
    
if(dimes == 1):
    print(f'{dimes} Dime')
if(dimes > 1):
    print(f'{dimes} Dimes')

if(nickels == 1):
    print(f'{nickels} Nickel')
if(nickels > 1):
    print(f'{nickels} Nickels')

if(pennies == 1):
    print(f'{pennies} Penny')
if(pennies > 1):
    print(f'{pennies} Pennies')
