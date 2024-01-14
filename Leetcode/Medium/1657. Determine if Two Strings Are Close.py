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
        count1 = Counter(word1)
        count2 = Counter(word2)
        chars1 = set(count1.keys())
        chars2 = set(count2.keys())
        values1 = Counter(count1.values())
        values2 = Counter(count2.values())
        return chars1 == chars2 and values1 == values2