"""
523. Continuous Subarray Sum
(Medium complexity)

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)  
        rems = set()  # множество остатков
        pref_rem = [0] * (n + 1)  # префиксные остатки
        for i in range(n):  # проходим по nums
            pref_rem[i + 1] = (pref_rem[i] + nums[i]) % k  # считаем префиксный остаток
            if pref_rem[i + 1] not in rems:  # если текущего остатка еще не было - добавляем предыдущий
                rems.add(pref_rem[i])
            else:  # иначе возвращаем True
                return True
        return False
