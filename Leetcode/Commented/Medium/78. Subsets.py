"""
78. Subsets
(Medium complexity)

Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]  # ответ
        for i in range(len(nums)):  # проходим по nums
            for j in range(len(answer)):  # проходим по answer
                answer.append(answer[j] + [nums[i]])  # добавляем в answer текущее из него + текущее из nums
        # ответ
        return answer




