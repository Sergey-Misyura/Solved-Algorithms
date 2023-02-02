"""
392. Is Subsequence
(Easy complexity)

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True
        if not t:
            return False

        ind_in_s = 0
        ind_in_t = 0

        while ind_in_s < len(s) and ind_in_t < len(t):
            if t[ind_in_t] == s[ind_in_s]:
                ind_in_s +=1
            ind_in_t +=1
        if ind_in_s == len(s):
            return True
        return False