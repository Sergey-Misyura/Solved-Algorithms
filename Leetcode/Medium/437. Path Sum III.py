"""
437. Path Sum III
(Medium complexity)

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def sumSearch(node, targetSum, targets):
            if not node:
                return 0
            hit = 0
            for target in targets:
                if not target - node.val:
                    hit += 1
            targets = [target - node.val for target in targets] + [targetSum]

            return hit + sumSearch(node.left, targetSum, targets) + sumSearch(node.right, targetSum, targets)

        return sumSearch(root, targetSum, [targetSum])

