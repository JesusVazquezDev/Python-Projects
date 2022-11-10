#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:42:36 2022

@author: jesusvazquez
"""


#  Use an except block to catch any ZeroDivisionError and output an exception message.
# Use another except block to catch any ValueError caused by invalid input and output
# an exception message.
user_num = -1
div_num = -1
try:
    user_num = input()
    user_num = int(user_num)
    div_num = input()
    div_num = int(div_num)
    result = user_num / div_num

except ZeroDivisionError:
    print('Zero Division Exception: integer division or modulo by zero')
    exit()

except ValueError:
    if div_num == -1:
        print(f'Input Exception: invalid literal for int() with base 10: \'{user_num}\'')
    else:
        print(f'Input Exception: invalid literal for int() with base 10: \'{div_num}\'')
    exit()

print(int(result))
    

    