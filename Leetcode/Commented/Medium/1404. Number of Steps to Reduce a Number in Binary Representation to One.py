"""
1404. Number of Steps to Reduce a Number in Binary Representation to One
(Medium complexity)

Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.
"""


class Solution:
    def numSteps(self, s: str) -> int:
        ans, tmp = 0, 0  # ответ и доп бит
        for i in range(len(s) - 1, 0, -1):  # проходим по битам справа налево до первого
            if not int(s[i]) ^ tmp:  # если число четное - добавляем одну операцию
                ans += 1
            else:  # если число нечетное - добавляем две операции и изменяем tmp
                ans += 2
                tmp = 1
        ans += 1 if not int(s[0]) ^ tmp else 0  # проверяем первый бит
        # ответ
        return ans
                
