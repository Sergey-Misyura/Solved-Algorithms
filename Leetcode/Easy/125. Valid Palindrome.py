"""
125. Valid Palindrome
(Easy complexity)

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing 
all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_normalized = re.sub('[^a-zA-Z0-9]', '', s.lower())
        
        return s_normalized == s_normalized [::-1]
