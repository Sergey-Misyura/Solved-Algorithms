"""
2441. Largest Positive Integer That Exists With Its Negative
(Easy complexity)

Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.
"""


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_d = dict()  # словарь номеров
        answer = -1  # ответ
        for num in nums:  # проходим по номерам
            if -num in nums_d:  # если -num есть в nums_d - обновляем answer
                answer = max(answer, abs(num))
            else:  # иначе добавляем num в словарь
                nums_d[num] = 1
        # ответ
        return answer