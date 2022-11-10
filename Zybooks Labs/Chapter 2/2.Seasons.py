#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:27:27 2022

@author: jesusvazquez
"""

input_month = input()
input_day = int(input())

if(input_day < 1 or input_day > 31):
    print("Invalid")
    exit()

spring = {'March', 'April', 'May', 'June'}
summer = {'June', 'July', 'August', 'September'}
autumn = {'September', 'October', 'November', 'December'}
winter = {'December', 'January', 'February', 'March'}

if input_month in spring:
    if input_month in summer:
        if input_day < 21:
            print('Spring')
        else:
            print('Summer')
    elif input_month in winter: 
        if input_day > 19:
            print('Spring')
        else:
            print('Winter')
    else:
        print('Spring')
        
elif input_month in summer:
    if input_month in autumn:
        if input_day < 22:
            print('Summer')
        else:
            print('Invalid')
    elif input_month in spring: 
        if input_day < 21:
            print('Spring4')
        else:
            print('Summer4')
    else:
        print('SummerF')
elif input_month in winter:
    if input_month in summer:
        if input_day > 21:
            print('Summer5')
        else:
            print('winter5')
    elif input_month in spring: 
        if input_day < 21:
            print('Spring5')
        else:
            print('Summer5')
    else:
        print('Winter')
elif input_month in autumn:
    if input_month in summer:
        if input_day > 21:
            print('Summer7')
        else:
            print('Autumn7')
    elif input_month in winter: 
        if input_day < 21:
            print('winter6')
        else:
            print('Autumn6')
    else:
        print('Autumn')
else:
    print("Invalid")
