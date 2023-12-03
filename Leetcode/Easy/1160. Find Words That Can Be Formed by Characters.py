"""
1160. Find Words That Can Be Formed by Characters
(Easy complexity)

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
"""

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        return sum(len(word) for word in words if chars_count >= Counter(word))