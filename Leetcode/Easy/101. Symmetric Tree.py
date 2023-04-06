"""
101. Symmetric Tree
(Easy complexity)

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(lf, rg):
            if lf and rg and lf.val == rg.val:
                return sym(lf.left, rg.right) and sym(lf.right, rg.left)
            return lf == rg

        return sym(root.left, root.right)


