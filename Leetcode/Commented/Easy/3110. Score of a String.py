"""
3110. Score of a String
(Easy complexity)

You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.
"""


class Solution:
    def scoreOfString(self, s: str) -> int:
        answer = 0  # ответ
        for i in range(len(s) - 1):  # проходим по строке
            answer += abs(ord(s[i]) - ord(s[i + 1]))  # увеличиваем ответ на abs разницу соседних символов
        return answer