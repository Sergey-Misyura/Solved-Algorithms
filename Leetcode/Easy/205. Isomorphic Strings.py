"""
205. Isomorphic Strings
(Easy complexity)

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_in_t, t_in_s = {}, {}

        for sym_in_s, sym_in_t in zip(s, t):
            
            if (sym_in_s not in s_in_t) and (sym_in_t not in t_in_s):
                s_in_t[sym_in_s], t_in_s[sym_in_t] = sym_in_t, sym_in_s

            elif s_in_t.get(sym_in_s) != sym_in_t or t_in_s.get(sym_in_t) != sym_in_s:
                return False
            
        return True