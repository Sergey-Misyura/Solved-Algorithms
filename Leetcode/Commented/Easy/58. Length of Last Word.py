"""
58. Length of Last Word
(Easy complexity)

Given a string s consisting of words and spaces, return the length of the last word in the string.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ln = 0  # длина слова
        cur = len(s) - 1  # указатель в s
        while s[cur] == ' ':  # проходим с конца, находим первый не пробельный символ
            cur -= 1
        while cur >= 0 and s[cur] != ' ':  # проходим дальше, считаем длину слова
            cur -= 1
            ln += 1

        # ответ
        return ln