#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:50:32 2022

@author: jesusvazquez
"""

class Solution:
    def runningSum(self, nums):
        for i in range(len(nums)):
            if(i != 0):
                nums[i] += nums[i-1]
        return nums

if __name__ == "__main__" :
    nums = [1,2,3,4]
    Solution.runningSum(nums)