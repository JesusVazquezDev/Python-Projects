#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:33:24 2022

@author: jesusvazquez
"""

def int_to_reverse_binary(x):
    return format(x, "b")[::-1]

def string_reverse(input_string):
    return input_string[::-1]

if __name__ == '__main__':
    # Type your code here.
    input_value = int_to_reverse_binary(int(input()))
    print(string_reverse(input_value))
    # Your code must call int_to_reverse_binary() to get 
    # the binary string of an integer in a reverse order.
    # Then call string_reverse() to reverse the string
    # returned from int_to_reverse_binary().

