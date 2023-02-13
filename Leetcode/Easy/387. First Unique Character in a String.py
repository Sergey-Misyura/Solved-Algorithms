"""
387. First Unique Character in a String
(Easy complexity)

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count_dict = collections.Counter(s)
        
        for indx, sym in enumerate(s):
            if count_dict[sym] == 1:
                return indx     
        return -1
            
       