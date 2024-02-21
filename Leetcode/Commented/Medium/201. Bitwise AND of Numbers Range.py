"""
201. Bitwise AND of Numbers Range
(Medium complexity)

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0  # количество сдвигов
        while left != right:
            # сдвигаем left и right на 1 бит вправо до нахождения их префикса
            left >>= 1; right >>= 1
            # увеличиваем счетчик сдвигов
            count += 1
        # сдвигаем полученный left налево на count бит
        return left << count