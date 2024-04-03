"""
287. Find the Duplicate Number
(Medium complexity)

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]  # быстрый, медленный указатели
        while True:  # пока указатели не сошлись
            slow, fast = nums[slow], nums[nums[fast]]  # двигаем левый и правый указатели
            if slow == fast: break  # если сошлись - остановка

        slow = nums[0]  # переносим медленный указатель
        while slow != fast:  # двигаем одинаково оба указателя, пока они снова не сойдуться
            slow, fast = nums[slow], nums[fast]

        # ответ
        return slow