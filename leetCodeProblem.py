# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:43:29 2019

@author: josep
"""
from typing import List


class Solution:
    def genRectangleSlice(self, superRect, startRow, startCol, length, width): # returns slice of the rectangle you requested
        assert (len(superRect) >= length > 0 and len(superRect[0]) >= width > 0), "Invalid lengths or widths for given superRect"
        resultingRectangle = [superRect[row][startCol:startCol + width] for row in range(startRow, startRow + length)]
        return resultingRectangle
    
    def sumRectangle(self, rectangle):
        total = 0
        for row in rectangle:
            total += sum(row)
        return total
        
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # Check all the rectangle slices possible. Return the one closest to k
        max_contendor = 0
        rows = len(matrix)
        if not rows:
            return 0
        presumedCols = len(matrix[0])
        if not presumedCols:
            return 0
        
        for startingRow in range(rows):
            for startingCol in range(presumedCols):
                for length in range(1, rows - startingRow + 1):
                    for width in range(1, presumedCols - startingCol + 1):
                        print(rows, presumedCols, startingRow, startingCol,length, width)
                        sliceSum = self.sumRectangle(self.genRectangleSlice(
                                matrix, startingRow, startingCol,length, width))
                        if max_contendor < sliceSum < k:
                            max_contendor = sliceSum
        return max_contendor



solution = Solution()
testMatrix = [[1,0,1],[0,-2,3]]
k = 2 # = maxRectangleSum

for row in testMatrix:
    print(row)
print(solution.maxSumSubmatrix(testMatrix, k))