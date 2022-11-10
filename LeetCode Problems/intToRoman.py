#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:53:03 2022

@author: jesusvazquez
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""
        
        I = 1
        IV = 4
        V = 5
        IX = 9
        X = 10
        XL = 40
        L = 50
        XC = 90
        C = 100
        CD = 400
        D = 500
        CM = 900
        M = 1000
        
        print(f'M: {num % M}')
        print(f'CM: {num % CM}')
        print(f'D: {num % D}')
        print(f'CD: {num % CD}')
        print(f'C: {num % C}')
        print(f'XC: {num % XC}')   
        print(f'L: {num % L}')
        print(f'XL: {num % XL}')   
        print(f'X: {num % X}')     
        print(f'IX: {num % IX}')
        print(f'V: {num % V}')
        print(f'IV: {num % IV}')
        print(f'I: {num % I}')
              
        if(num % M != num):
            while(num != num % M):
                output += 'M'
                num -= M
                
        if(num % CM != num):
            while(num != num % CM):
                output += 'CM'
                num -= CM
        
        if(num % D != num):
            while(num != num % D):
                output += 'D'
                num -= D
        
        if(num % CD != num):
            while(num != num % CD):
                output += 'CD'
                num -= CD
        
        if(num % C != num):
            while(num != num % C):
                output += 'C'
                num -= C
                
        if(num % XC != num):
            while(num != num % XC):
                output += 'XC'
                num -= XC
        
        if(num % L != num):
            while(num != num % L):
                output += 'L'
                num -= L

        if(num % XL != num):
            while(num != num % XL):
                output += 'XL'
                num -= XL               
                
        if(num % X != num):
            while(num != num % X):
                output += 'X'
                num -= X
                
        if(num % IX != num):
            while(num != num % IX):
                output += 'IX'
                num -= IX                
                
        if(num % V != num):
            while(num != num % V):
                output += 'V'
                num -= V
        
        if(num % IV != num):
            while(num != num % IV):
                output += 'IV'
                num -= IV    
    
        if(num % I != num):
            while(num != num % I):
                output += 'I'
                num -= I
                
        return output
    
if __name__ == "__main__":
    num = 58
    Solution.intToRoman(num)