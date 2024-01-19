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
        target = Counter(t)
        remain = len(t)
        start, end = 0, 0
        lf = 0

        for rg, char in enumerate(s, 1):
            if target[char] > 0:
                remain -= 1
            target[char] -= 1
            if remain == 0:
                while lf < rg and target[s[lf]] < 0:
                    target[s[lf]] += 1
                    lf += 1
                target[s[lf]] += 1
                remain += 1

                if end == 0 or rg - lf < end - start:
                    start, end = lf, rg

                lf += 1

        return s[start:end]


