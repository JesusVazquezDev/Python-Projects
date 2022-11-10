#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:45:58 2022

@author: jesusvazquez
"""

class Solution:
    def pivotIndex(self, nums):
        sumL = 0
        sumR = sum(nums)
        for i in range(len(nums)):
            sumR -= nums[i]
            if sumL == sumR:
                return i
            sumL += nums[i]
        return -1
    
if __name__ == "__main__":
    
    nums = nums = [1,7,3,6,5,6]
    
    Solution.pivotIndex(nums)