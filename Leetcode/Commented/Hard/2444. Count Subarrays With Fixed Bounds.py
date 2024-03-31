"""
2444. Count Subarrays With Fixed Bounds
(Hard complexity)

You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.
"""


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0  # ответ
        last_before = lf = rg = -1  # индекс последнего вхождения числа до minK и maxK, индекс последнего minK, индекс последнего maxK

        for i, num in enumerate(nums):  # проходим по nums
            if num < minK or num > maxK:  # если число не входит в диапазон [minK, maxK] - меняем last_before
                last_before = i

            if num == minK:  # при minK сдвигаем lf
                lf = i

            if num == maxK:  # при maxK сдвигаем rg
                rg = i

            # число подмассивов с искомыми границами - длина от самомого раннего из lf и rg до last_before
            answer += max(0, min(lf, rg) - last_before)

        # ответ
        return answer

