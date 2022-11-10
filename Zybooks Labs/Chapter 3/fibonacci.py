#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:34:54 2022

@author: jesusvazquez
"""

def fibonacci(n):
    i = 0
    prev = 0
    nextNum = 1
    result = 0
    if n < 0:
        return -1
        
    for i in range(n):
        result = prev + nextNum
        prev = nextNum
        nextNum = result
        i+= 1
        
    return prev
        


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')