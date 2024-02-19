"""
231. Power of Two
(Easy complexity)

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2^x.
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        bin_n = bin(n)
        return bin_n[0] != '-' and bin_n[2:].count('1') == 1