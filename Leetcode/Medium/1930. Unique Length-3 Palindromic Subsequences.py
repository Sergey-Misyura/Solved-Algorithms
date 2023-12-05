"""
1930. Unique Length-3 Palindromic Subsequences
(Medium complexity)

Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
"""


class Solution:
    def countPalindromicSubsequence(self, s):
        ans = 0
        for sym in string.ascii_lowercase:
            from_, to_ = s.find(sym), s.rfind(sym)
            if from_ > -1:
                ans += len(set(s[from_ + 1: to_]))
        return ans
