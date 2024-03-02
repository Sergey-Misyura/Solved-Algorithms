"""
977. Squares of a Sorted Array
(Easy complexity)

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)  # массив ответов
        lf, rg = 0, len(nums) - 1  # два указателя
        while lf <= rg:
            lf_num, rg_num = abs(nums[lf]), abs(nums[rg])  # модули чисел lf, rg
            # если lf_num больше rg_num добавляем lf_num**2 в ответ
            if lf_num > rg_num:
                ans[rg - lf] = lf_num ** 2
                lf += 1
            # инчае добавляем rg_num**2 в ответ
            else:
                ans[rg - lf] = rg_num ** 2
                rg -= 1
        # ответ
        return ans

