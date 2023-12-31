"""
1624. Largest Substring Between Two Equal Characters
(Easy complexity)
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        idx = {}
        total = -1
        for i in range(len(s)):
            if s[i] in idx:
                total = max(total, i - idx[s[i]] - 1)
            else:
                idx[s[i]] = i

        return total