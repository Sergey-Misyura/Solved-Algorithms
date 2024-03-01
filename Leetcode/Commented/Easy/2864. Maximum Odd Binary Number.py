"""
2864. Maximum Odd Binary Number
(Easy complexity)

You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.
"""


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)  # длина бинарного числа
        ones_count = s.count('1')  # количество единиц в бинарном числе
        ans = ['0']*n  # массив ответа
        ans[-1] = '1'  # ставим последнюю цифру 1 для нечетности
        for i in range(ones_count - 1):  # ставим первые числа 1 для макс числа
            ans[i] = '1'

        # ответ
        return ''.join(ans)