"""
1704. Determine if String Halves Are Alike
(Easy complexity)

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n, count_1, count_2 = len(s), 0, 0
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        for i in range(n//2):
            count_1 += 1 if s[i] in vowels else 0
            count_2 += 1 if s[n-i-1] in vowels else 0
        return count_1 == count_2