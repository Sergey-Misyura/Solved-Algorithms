"""
5. Longest Palindromic Substring
(Medium complexity)

Given a string s, return the longest
palindromic substring in s.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, ans = len(s), ""

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i, j = i - 1, j + 1
            return s[i + 1:j]

        for k in range(n):
            ans = max(helper(k, k), helper(k, k + 1), ans, key=len)
        return ans