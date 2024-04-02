"""
238. Product of Array Except Self
(Medium complexity)

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)  # длина nums
        suf_prod = [1] * (n + 1)  # суффиксное произведение nums
        ans = [1] * n  # массив ответа
        suf_prod[-2] = nums[-1]  # заполнение
        for i in range(n - 2, 0, -1):  # подсчитываем элементы суфф произведения
            suf_prod[i] = suf_prod[i + 1] * nums[i]

        for i in range(n):  # проходим по nums
            ans[i] = suf_prod[i] * suf_prod[i + 1]  # записываем ответ как произведение слева * на произведение справа
            suf_prod[i + 1] = suf_prod[i] * nums[i]  # пересчитываем на префиксное произведение

        # ответ
        return ans