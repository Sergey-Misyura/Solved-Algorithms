"""
1509. Minimum Difference Between Largest and Smallest Value in Three Moves
(Medium complexity)

You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.
"""


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()  # сортируем массив и находим мин разницу при замене 3х элементов с разных концов
        return min(b - a for a, b in zip(nums[:4], nums[-4:]))