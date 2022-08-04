"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.
Example 1:
Input: x = 1, y = 4
Output: 2
"""
#Solution:

class Solution(object):
    def hammingDistance(self, x, y):
        count=0
        for i in range(31,-1,-1):
            x1= x>>i&1
            y1 = y>>i&1
            count+= not(x1==y1)
        return count