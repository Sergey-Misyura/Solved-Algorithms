"""
39. Combination Sum
(Medium complexity)

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""


class Solution(object):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtr(target, curr, k):
            if target == 0:
                self.answer.append(curr)

            if target < 0 or k >= len(candidates):
                return

            for i in range(k, len(candidates)):
                backtr(target - candidates[i], curr + [candidates[i]], i)

        self.answer = []
        backtr(target, [], 0)

        return self.answer


