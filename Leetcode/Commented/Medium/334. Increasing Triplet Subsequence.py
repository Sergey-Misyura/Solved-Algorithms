"""
334. Increasing Triplet Subsequence
(Medium complexity)

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_num = second_min_num = float('inf')  # первый и второй минимумы
        for num in nums:  # проходим по nums
            if num <= min_num:  # обновляем первый минимум
                min_num = num
            elif num <= second_min_num:  # иначе обновляем второй мнимум
                second_min_num = num
            else:  # если нашли число больше обоих минимумов - ответ True
                return True
        # если прошли все nums - ответ False
        return False
