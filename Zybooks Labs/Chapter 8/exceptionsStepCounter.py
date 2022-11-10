#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:43:07 2022

@author: jesusvazquez
"""

# Define your method here
def steps_to_miles(steps):
    if(steps< 0):
        raise ValueError('Exception: Negative step count entered.')
    
    return steps/2000

if __name__ == '__main__':
    # Type your code here.
    steps = int(input())
    try:
        result = steps_to_miles(steps)
        print(f'{result:.2f}')
    except ValueError as excpt:
        print(excpt)
        exit()