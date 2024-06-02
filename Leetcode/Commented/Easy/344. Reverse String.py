"""
344. Reverse String
(Easy complexity)

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lf, rg = 0, len(s) - 1  # левый, правый указатели
        while lf < rg:  # пока указатели не сошлись, меняем местами значения в строке
            s[lf], s[rg] = s[rg], s[lf]
            lf += 1
            rg -= 1