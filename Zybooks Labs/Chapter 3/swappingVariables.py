#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:33:53 2022

@author: jesusvazquez
"""

def swap_values(user_val1, user_val2, user_val3, user_val4):
    return user_val2, user_val1, user_val4, user_val3

if __name__ == '__main__': 
    
   user_val2, user_val1, user_val4, user_val3 = swap_values(int(input()), int(input()), int(input()), int(input()))
   print(f'{user_val2} {user_val1} {user_val4} {user_val3}')