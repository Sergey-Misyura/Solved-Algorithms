"""
2131. Longest Palindrome by Concatenating Two Letter Words
(Medium complexity)

You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.
"""

from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        counter, ans = defaultdict(int), 0
        for w in words:
            rev = w[::-1]
            if rev in counter and counter[rev] > 0:
                ans += 4
                counter[rev] -= 1
            else:
                counter[w] +=1


        for key in counter.keys():
            if key[-1]==key[0] and counter[key] > 0:
                ans += 2
                break
        return ans