"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""



class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        t,b = 0, len(matrix) - 1

        while t <= b:
            m = (t+b)//2
            
            if target < matrix[m][0]:
                b = m - 1
            
            elif target > matrix[m][-1]:
                t =m +1
            
            else:
                break
        
        if not (t <= b):
            return False
        
        row = (t+b)//2
        l,r =0, len(matrix[0])-1

        while l <= r:
            m = (l+r) //2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        
        return False