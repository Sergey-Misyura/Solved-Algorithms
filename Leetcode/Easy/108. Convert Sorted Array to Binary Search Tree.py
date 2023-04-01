"""
108. Convert Sorted Array to Binary Search Tree
(Medium complexity)

Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced
 binary search tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums))

    def helper(self, nums, left, right):
        if left == right:
            return None

        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, left, mid)
        node.right = self.helper(nums, mid+1, right)

        return node