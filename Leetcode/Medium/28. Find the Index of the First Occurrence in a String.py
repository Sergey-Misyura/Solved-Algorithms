"""
28. Find the Index of the First Occurrence in a String
(Medium complexity)

Given two strings needle and haystack, return the index of the first occurrence 
of needle in haystack, or -1 if needle is not part of haystack.
"""

import re

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        occurrence  = re.search(needle, haystack)
        return occurrence.start() if occurrence else -1
        