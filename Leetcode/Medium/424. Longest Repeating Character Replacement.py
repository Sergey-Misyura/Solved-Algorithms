"""
424. Longest Repeating Character Replacement
(Medium complexity)

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        start, freq, max_freq, result = 0, {}, 0, 0

        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            max_freq = max(max_freq, freq[s[end]])

            res_exist = (k >= end - start + 1 - max_freq)
            if not res_exist:
                freq[s[start]], start = freq[s[start]] - 1, start+1

            result = end - start + 1

        return result