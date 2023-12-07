"""
1903. Largest Odd Number in String
(Easy complexity)

You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.
"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while i > -1 and (int(num[i]) % 2) == 0:
            i -= 1

        return num[:i + 1]