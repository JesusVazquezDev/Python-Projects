#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:39:59 2022

@author: jesusvazquez
"""

services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()

print('ZyCar Wash')
print(f'Base car wash -- ${base_wash}')

if(service_choice1 != '-'):
    price = services.get(service_choice1,'na')
    print(f'{service_choice1} -- ${price}')
    total += price
    
if(service_choice2 != '-'):
    price2 = services.get(service_choice2,'na')
    print(f'{service_choice2} -- ${price2}')
    total += price2
    
print('----')

total += base_wash
print(f'Total price: ${total}')