#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:34:21 2022

@author: jesusvazquez
"""

def exact_change(currency):

    if(currency == 0):
        return 0,0,0,0
    
    num_quarters = currency// 25
    currency -= 25 * num_quarters
    
    num_dimes = currency // 10
    currency -= 10 * num_dimes
    
    num_nickels = currency // 5
    currency -= 5 * num_nickels
    
    num_pennies = currency // 1
    currency -= 1 * num_pennies

    return num_pennies, num_nickels, num_dimes, num_quarters

if __name__ == '__main__': 
    input_val = int(input())  
    
    if(input_val == 0):
        print('no change')
        exit()
        
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)
    
    if(num_pennies == 1):
        print(f'{num_pennies} penny')
    if(num_pennies > 1):
        print(f'{num_pennies} pennies')
    
    if(num_nickels == 1):
        print(f'{num_nickels} nickel')
    if(num_nickels > 1):
        print(f'{num_nickels} nickels')

    if(num_dimes == 1):
        print(f'{num_dimes} dime')
    if(num_dimes > 1):
        print(f'{num_dimes} dimes')
        
    if(num_quarters == 1):
        print(f'{num_quarters} quarter')
    if(num_quarters > 1):
        print(f'{num_quarters} quarters')
        