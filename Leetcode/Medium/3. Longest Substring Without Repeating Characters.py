"""
3. Longest Substring Without Repeating Characters
(Medium complexity)

Given a string s, find the length of the longest
substring
 without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = 0
        prev = [-1] * 128
        max_len = 0

        for i in range(len(s)):
            sym_idx = ord(s[i])
            if prev[sym_idx] >= last:
                last = prev[sym_idx] + 1
            prev[sym_idx] = i
            max_len = max(max_len, i - last + 1)

        return max_len


