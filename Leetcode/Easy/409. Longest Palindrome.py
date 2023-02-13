"""
409. Longest Palindrome
(Easy complexity)

Given a string s which consists of lowercase or uppercase letters, return the length of 
the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""

import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        for v in collections.Counter(s).items():
            ans += v[1] // 2 * 2
            if ans % 2 == 0 and v[1] % 2 == 1:
                ans += 1
        
        return int(ans)