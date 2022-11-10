#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:24:57 2022

@author: jesusvazquez
"""

miles_per_gallon = float(input())
cost_per_gallon = float(input())

# Cost for 20 miles
q1 = (20 / miles_per_gallon) * cost_per_gallon
q2 = (75 / miles_per_gallon) * cost_per_gallon
q3 = (500 / miles_per_gallon) * cost_per_gallon


print(f'{q1:.2f} {q2:.2f} {q3:.2f}')