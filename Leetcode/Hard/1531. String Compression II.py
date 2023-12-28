"""
1531. String Compression II
(Hard complexity)

Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.
"""


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(i, prev, prev_cnt, k):
            if k < 0:
                return inf
            if i == len(s):
                return 0
            delete = dp(i + 1, prev, prev_cnt, k - 1)
            if s[i] == prev:
                keep = dp(i + 1, prev, prev_cnt + 1, k)
                if prev_cnt in [1, 9, 99]:
                    keep += 1
            else:
                keep = dp(i + 1, s[i], 1, k) + 1

            return min(delete, keep)

        return dp(0, '', 0, k)

