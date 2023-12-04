"""
2264. Largest 3-Same-Digit Number in String
(Easy complexity)

You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
"""

class Solution:
    def largestGoodInteger(self, num: str) -> str:

        return max(num[i] if num[i]==num[i-1]==num[i-2] else '' for i in range(2, len(num)))*3