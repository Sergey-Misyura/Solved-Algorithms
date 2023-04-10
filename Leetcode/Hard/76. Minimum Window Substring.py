"""
76. Minimum Window Substring
(Medium complexity)

Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        char_count, len_substr = collections.Counter(t), len(t)
        first = min_first = min_second = 0

        for second, char in enumerate(s, 1):
            len_substr = len_substr - 1 if char_count[char] > 0 else len_substr
            char_count[char] -= 1

            if len_substr == 0:

                while first < second and char_count[s[first]] < 0:
                    char_count[s[first]] += 1
                    first += 1

                if min_second == 0 or second - first <= min_second - min_first:
                    min_second, min_first = second, first

        return s[min_first:min_second]


