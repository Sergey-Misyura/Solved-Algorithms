"""
724. Find Pivot Index
(Easy complexity)

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)  # длина nums
        pref_sum = [0] * (n + 1)  # массив преф сумм
        suf_sum = [0] * (n + 1)  # массив суф сумм
        for i in range(n):  # заполняем массив преф сумм
            pref_sum[i + 1] = pref_sum[i] + nums[i]
        for i in range(n - 1, -1, -1):  # заполняем массив суф сумм
            suf_sum[i] = suf_sum[i + 1] + nums[i]

        for i in range(n):  # проходим по массивам pref_sum и suf_sum
            if pref_sum[i] == suf_sum[i + 1]:  # если сумма слева от индекса равна сумме справа - возвращаем индекс
                return i
        # иначе возвращаем -1
        return -1