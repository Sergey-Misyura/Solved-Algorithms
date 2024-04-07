"""
1657. Determine if Two Strings Are Close
(Medium complexity)

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1word2 , and false otherwise.
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)  # счетчик букв word1
        count2 = Counter(word2)  # счетчик букв word2
        chars1 = set(count1.keys())  # уникальные буквы в word1
        chars2 = set(count2.keys())  # уникальные буквы в word2
        values1 = Counter(count1.values())  # счетчик числа повторений букв в word1
        values2 = Counter(count2.values())  # счетчик числа повторений букв в word2
        # если число уникальных букв совпадает, и счетчики числа повторений букв совпадают,
        # то есть для ответа мы можем преобразовать одни буквы в другие - ответ True
        return chars1 == chars2 and values1 == values2