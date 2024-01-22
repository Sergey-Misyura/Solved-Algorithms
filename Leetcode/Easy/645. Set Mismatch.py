"""
645. Set Mismatch
(Easy complexity)

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        n_sum = int(n * (n + 1)/2)
        set_sum = sum(set(nums))
        nums_sum = sum(nums)

        return [nums_sum - set_sum, n_sum - set_sum]
