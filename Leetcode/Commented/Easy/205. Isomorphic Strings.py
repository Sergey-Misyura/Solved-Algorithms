"""
205. Isomorphic Strings
(Easy complexity)

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1, m2, n = [-1] * 256, [-1] * 256, len(s)  # массивы индексов мест замен для букв в s и t, длина строк
        for i in range(n):  # проходим по s и t
            # если индексы места замены оказались разные, то есть мы до этого меняли одну букву на другую - ответ False
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False
            m1[ord(s[i])] = i  # записываем индекс места замены для s
            m2[ord(t[i])] = i  # записываем индекс места замены для t
        # ответ
        return True