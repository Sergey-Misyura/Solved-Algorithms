"""
238. Product of Array Except Self
(Medium complexity)

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf_prod = [1] * (n + 1)
        ans = [1] * n
        suf_prod[-2] = nums[-1]
        for i in range(n - 2, 0, -1):
            suf_prod[i] = suf_prod[i + 1] * nums[i]

        prev = 1
        for i in range(n):
            ans[i] = suf_prod[i] * suf_prod[i + 1]
            suf_prod[i + 1] = suf_prod[i] * nums[i]

        return ans