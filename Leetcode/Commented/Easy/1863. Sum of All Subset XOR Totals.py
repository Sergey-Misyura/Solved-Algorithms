"""
1863. Sum of All Subset XOR Totals
(Easy complexity)

The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums.

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
"""


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)  # длина
        total_or = 0  # результат OR для всех чисел
        for i in range(n):
            total_or |= nums[i]
        # возвращаем total_or * общее количество подмножеств чисел 2 ** т
        return total_or * (1 << (n - 1))
