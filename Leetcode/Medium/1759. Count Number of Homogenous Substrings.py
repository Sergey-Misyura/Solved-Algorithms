"""
1759. Count Number of Homogenous Substrings
(Medium complexity)

Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.
"""

class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10 ** 9 + 7
        lf = 0
        ans = 0
        for rg in range(len(s)):
            if s[lf] == s[rg]:
                ans += rg - lf + 1
            else:
                ans, lf = ans + 1, rg

        return ans % mod
