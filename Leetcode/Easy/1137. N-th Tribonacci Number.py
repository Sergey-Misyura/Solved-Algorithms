"""
1137. N-th Tribonacci Number
(Easy complexity)

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:  # для 0 значения
            return 0
        if n == 1 or n == 2:  # для 1 и 2 значений
            return 1
        t0, t1, t2 = 0, 1, 1
        for _ in range(n - 2):  # цикл для получения номеров Трибоначчи
            t2, t1, t0 = t0 + t1 + t2, t2, t1
        # ответ
        return t2
