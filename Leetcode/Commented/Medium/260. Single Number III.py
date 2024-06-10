"""
260. Single Number III
(Medium complexity)

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0  # общий xor
        for num in nums:  # обновляем xor
            xor ^= num
        mask = xor & -xor  # ставим самый правый бит в 1 для разделения 2х чисел
        ans1, ans2 = 0, 0  # ответ 1 и 2
        for num in nums:  # проходим по nums
            if num & mask:  # если у числа самый правый бит установлен - его xor c ans1
                ans1 ^= num
            else:  # иначе его xor c ans2
                ans2 ^= num
        # ответ
        return ans1, ans2