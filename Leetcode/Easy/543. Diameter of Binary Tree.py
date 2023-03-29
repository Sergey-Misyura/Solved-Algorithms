"""
543. Diameter of Binary Tree
(Easy complexity)

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def mlps(root): #max len path search
            if not root:
                return -1, 0
            left, right = mlps(root.left), mlps(root.right)
            return max(left[0], right[0]) + 1, max(left[1], right[1], 2 + left[0] + right[0])

        return mlps(root)[1]