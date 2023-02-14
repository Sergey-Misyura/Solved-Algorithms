"""
844. Backspace String Compare
(Easy complexity)

Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a, b = '', ''

        for i in range(0, len(s)):
            a = a+s[i] if s[i]!='#' else a[:-1]

        for j in range(0, len(t)):
            b = b+t[j] if t[j]!='#' else b[:-1]

        return a==b