#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:40:54 2022

@author: jesusvazquez
"""

def get_age():
    age = int(input())
    # TODO: Raise exception for invalid ages
    # The adult's age between the ages of 18 and 75 inclusive
    if( age < 18 or age > 75) :
        raise ValueError("Invalid age.")

    return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    # 70% of the difference between 220 and the person's age respectively.
    heart_rate = 220 - age
    return heart_rate * 0.7

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        result = fat_burning_heart_rate(age) 
    except ValueError as excpt:
        print(excpt)
        print("Could not calculate heart rate info.")
        exit()
        
    print(f'Fat burning heart rate for a 35 year-old: {result} bpm')
    