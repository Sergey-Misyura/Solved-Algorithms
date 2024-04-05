"""
643. Maximum Average Subarray I
(Easy complexity)

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = ans = sum(nums[:k])  # текущая сумма в окне k и ответ
        for i in range(k, len(nums)):  # проходим по оставшимся числам в массиве
            cur = cur + nums[i] - nums[i - k]  # меняем сумму в окне k
            ans = max(ans, cur)  # обновляем ответ
        # ответ
        return ans / k