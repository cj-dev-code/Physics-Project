# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 22:15:49 2019

@author: josep
"""

from functools import reduce
from typing import List
class Solution:
    def twoSum(self, nums, k, avoid=None):
        print(nums)    
        solutions = set()
        k_complement = {}
        for num in nums:
            #if num == -k:
            #    continue
            if type(k_complement.get(num, False)) == bool:
                k_complement[k - num] = num
            else:

                solutions.add(tuple(sorted([num, k_complement[num], -k])))
        return solutions
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sols = set()
        clone = nums[:]
        for index, item in enumerate(nums):
            sols |= self.twoSum(clone, -1*clone.pop(index))
            clone.insert(index, item)
            
        #for k in nums:
        #    sols |= self.twoSum(nums, -k)
        return list(sols)
solution = Solution()
print(solution.threeSum([0,0,0]))