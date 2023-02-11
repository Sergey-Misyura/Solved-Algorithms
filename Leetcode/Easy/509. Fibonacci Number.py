"""
509. Fibonacci Number
(Easy complexity)

The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
"""

class Solution:
    def fib(self, n: int) -> int:

        if n==0: return 0
        elif n==1: return 1
        else:
            prev, res = 0, 1
            for _ in range(n-1):
                prev, res = res, prev+res 

            return res