"""
647. Palindromic Substrings
(Medium complexity)

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            # odd
            count, lf, rg = 0, i, i
            while lf >= 0 and rg <= n - 1 and s[lf] == s[rg]:
                lf, rg = lf - 1, rg + 1
                count += 1
            ans += count

            # even
            count, lf, rg = 0, i, i + 1
            while lf >= 0 and rg <= n - 1 and s[lf] == s[rg]:
                lf, rg = lf - 1, rg + 1
                count += 1
            ans += count

        return ans