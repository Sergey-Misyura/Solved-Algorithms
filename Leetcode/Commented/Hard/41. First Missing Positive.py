"""
41. First Missing Positive
(Hard complexity)

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # проходим по nums, заменяем отрицательные и больше n на n + 1, ограничивая сверху n + 1, и превращая массив в > 0
        # если есть отрицательные или больше n - искомое число находится до n + 1, в противном случае если все числа от 1 до n return n + 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):  # проходим по nums, ставим '-' флаги для встреченных чисел от 1 до n в местах nums[число]
            if abs(nums[i]) <= n:
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])

        for i in range(n):  # снова проходим по nums, если встретили число без флага '-', тогда выдаем его индекс + 1
            if nums[i] > 0:
                return i + 1
        # ответ при массиве из чисел от 1 до n
        return n + 1