"""
43. Multiply Strings
(Medium complexity)

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def multiply(self, num1, num2):

        res = [0] * (len(num1) + len(num2))

        for idx1, sym1 in enumerate(reversed(num1)):
            for idx2, sym2 in enumerate(reversed(num2)):
                res[idx1 + idx2] += int(sym1) * int(sym2)
                res[idx1 + idx2 + 1] += res[idx1 + idx2] // 10
                res[idx1 + idx2] %= 10

        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return ''.join(map(str, res[::-1]))
