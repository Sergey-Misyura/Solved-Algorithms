"""
2486. Append Characters to String to Make Subsequence
(Medium complexity)

You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
"""


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        idx_t = 0  # индекс в t
        for sym in s:  # проходим по символам в s
            if idx_t < n and t[idx_t] == sym:  # если не вышли за пределы t и текущий в t равен в s
                idx_t += 1  # сдвигаем индекс в t
        # возвращаем число недостающих символов
        return n - idx_t