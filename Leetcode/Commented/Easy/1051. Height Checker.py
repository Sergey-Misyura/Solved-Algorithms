"""
1051. Height Checker
(Easy complexity)

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].
"""

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = Counter(heights)  # счетчик высот
        min_key, max_key = min(counts.keys()), max(counts.keys())  # мин, макс для цикла по росту
        ans, i = 0, 0  # ответ, указатель на heights
        for key in range(min_key, max_key + 1):  # проходим по разным ростам
            for _ in range(counts.get(key, 0)):  # проходим по количеству одинаковых в counts
                if heights[i] != key:  # если человек не на свое месте - увеличиваем ans
                    ans += 1
                i += 1
        # ответ
        return ans
