"""
442. Find All Duplicates in an Array
(Medium complexity)

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []  # массив ответа
        for num in nums:  # проходим по числам
            if nums[abs(num) - 1] < 0:  # если число на индексе num - 1 отрицательное - значит уже встречали его, добавляем в ответ
                ans.append(abs(num))
            else: # иначе ставим флаг, меняем знак у числа с индексом num - 1
                nums[abs(num) - 1] *= -1
        return ans