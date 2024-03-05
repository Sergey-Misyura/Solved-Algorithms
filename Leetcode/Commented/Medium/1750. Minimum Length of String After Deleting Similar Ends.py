"""
1750. Minimum Length of String After Deleting Similar Ends
(Medium complexity)

Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return minimum length s after performing the above operation any number of times (possibly zero times).
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        lf, rg = 0, len(s) - 1  # левый и правый указатели
        while lf < rg and s[lf] == s[rg]:  # пока указатели не сошлись и крайние символы равны
            cur = s[lf]  # текущий проверяемый символ
            while lf <= rg and s[lf] == cur:  # убираем левые повторяющиеся символы
                lf += 1
            while rg >= lf and s[rg] == cur:  # убираем правые повторяющиеся символы
                rg -= 1
        # ответ - длина оставшейся строки
        return rg - lf + 1
