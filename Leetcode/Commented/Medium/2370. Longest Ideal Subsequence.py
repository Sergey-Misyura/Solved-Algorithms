"""
2370. Longest Ideal Subsequence
(Medium complexity)

You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

t is a subsequence of the string s.
The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.
"""


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 128  # массив динамики - самая длинная иделаьная подпоследовательность оканчивающаяся на i
        for sym in s:  # проходим по символам
            i = ord(sym)  # код символа
            dp[i] = max(dp[i - k: i + k + 1]) + 1  # берем max подпоследовательность из k слева и k справа символов в dp,
            # так как можем убрать промежуточные символы для получения такой подпоследовательности
        # ответ max
        return max(dp)