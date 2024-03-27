"""
713. Subarray Product Less Than K
(Medium complexity)

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0  # общее число подмассив с произведением < k
        lf = 0  # левая граница раздвижного окна
        cur_prod = 1  # текущее произведение подмассива
        for rg in range(len(nums)): # проходим правой границей по nums
            cur_prod *= nums[rg]  # увелчичиваем произведение
            while lf <= rg and cur_prod >= k:  # сдвигаем левую границу до произведение < k и до rg
                cur_prod /= nums[lf]  # уменьшаем произведение
                lf += 1
            count += rg - lf + 1 # увеличиваем count на количество элементов в окне
        # ответ
        return count