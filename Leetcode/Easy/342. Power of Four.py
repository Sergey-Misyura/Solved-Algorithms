"""
342. Power of Four

(Easy complexity)

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 0:
            return False
        binary = bin(n)[2:]
        return binary[-3::-2].count('1')==1 and binary[-2::-2].count('1')==0 and binary[-1]=='0'