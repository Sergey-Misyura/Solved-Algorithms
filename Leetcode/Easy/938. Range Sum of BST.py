"""
938. Range Sum of BST
(Easy complexity)

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node):
            if node == None:
                return 0
            total = 0
            if low <= node.val <= high:
                total += node.val

            return total + dfs(node.left) + dfs(node.right)

        return dfs(root)
