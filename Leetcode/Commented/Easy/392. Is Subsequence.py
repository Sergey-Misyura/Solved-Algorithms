"""
392. Is Subsequence
(Easy complexity)

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cur = 0  # текущий указатель на последний символ из s в t
        n = len(t)  # длина t
        for sym in s:  # проходим по символам s
            if cur >= n:  # если вышли за t - ответ False
                return False
            match = re.search(sym, t[cur:])  # находим символ в t обрезанном по cur
            if not match:  # если не нашли символ - False
                return False
            else:  # если нашли - переносим указатель
                cur += match.start() + 1
        # ответ
        return True