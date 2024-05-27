"""
1608. Special Array With X Elements Greater Than or Equal X
(Easy complexity)

You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
"""

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse = True)  # сортировка по убыванию
        nums = nums + [-1]  # добавляем фиктивную -1
        for i in range(len(nums) - 1):  # проходим до последнего числа по nums
            # когда встречаем 2 разных соседних номера, и если i + 1(количество чисел >=) находится между ними - возвращаем i + 1
            if nums[i] != nums[i + 1] and nums[i] >= i + 1 > nums[i + 1]:
                return i + 1
        # если не нашли ответ - возвращаем -1
        return -1