"""
1493. Longest Subarray of 1's After Deleting One Element
(Medium complexity)

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1  # количество замен
        lf = 0  # левая граница окна
        for rg in range(len(nums)):  # проходим правой границей окна по nums
            if nums[rg] == 0:  # если встретили 0 - уменьшаем k
                k -= 1
            if k < 0:  # если уменьшили k дважды, двигаем левую границу, восстанавливаем k до 0
                if nums[lf] == 0:
                    k += 1
                lf += 1
        # ответ - длина окна
        return rg - lf