"""
974. Subarray Sums Divisible by K
(Medium complexity)

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.
"""


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref_rem = 0  # префиксный остаток от деления
        counts = [1] + [0] * k  # счетчик числа уже встреченных остатков
        ans = 0  # ответ
        for num in nums:  # проходим по nums
            pref_rem = (pref_rem + num) % k  # пересчитываем остаток
            ans += counts[pref_rem]  # увеличиваем ответ на число уже встреченных таких остатков (остаток подмассива между ними 0)
            counts[pref_rem] += 1  # увеличиваем счетчик counts

        return ans