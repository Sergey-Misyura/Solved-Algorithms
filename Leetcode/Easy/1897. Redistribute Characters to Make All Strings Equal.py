"""
1897. Redistribute Characters to Make All Strings Equal
(Easy complexity)

You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.
"""


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = [0] * 26
        for word in words:
            for sym in word:
                freq[ord(sym) - ord('a')] += 1

        n = len(words)
        for val in freq:
            if val % n != 0:
                return False

        return True
