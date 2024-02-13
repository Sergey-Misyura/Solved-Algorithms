"""
2108. Find First Palindromic String in the Array
(Easy complexity)

Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
"""

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for word in words:
            lf, rg = 0, len(word) - 1
            palindrom = True
            while lf < rg:
                if word[lf] != word[rg]:
                    palindrom = False
                    break
                lf += 1; rg -= 1

            if palindrom:
                return word

        return ""
