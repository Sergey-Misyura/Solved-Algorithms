"""
2709. Greatest Common Divisor Traversal
(Hard complexity)

You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.
"""


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:  # если 1 число ответ True
            return True
        if 1 in nums:  # если 1 в числах - ответ False
            return False

        nums = sorted(set(nums), reverse = True)  # сортируем уникальные числа
        n = len(nums)  # длина полученного массива
        for i in range(n-1):  # проходим по числам
            for j in range(i+1, n):  # проходим по соседям справа от числа
                if gcd(nums[i], nums[j]) > 1:  # если НОД > 1 - умножаем соседа на текущее число
                    nums[j]*= nums[i]
                    break
            else:  # если не нашли среди соседей числа у которого НОД с текущим > 1 - ответ False
                return False
        # ответ при прохождении - True
        return True
