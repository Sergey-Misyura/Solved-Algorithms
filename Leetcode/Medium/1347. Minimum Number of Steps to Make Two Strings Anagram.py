"""
1347. Minimum Number of Steps to Make Two Strings Anagram
(Medium complexity)

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
"""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        words = [0] * 26
        for sym in s:
            words[ord(sym) - 97] += 1

        replaces = 0
        for sym in t:
            i = ord(sym) - 97
            if words[i] > 0:
                words[i] -= 1
            else:
                replaces += 1

        return replaces