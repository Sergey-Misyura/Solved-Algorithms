"""
110. Balanced Binary Tree
(Easy complexity)

Given a binary tree, determine if it is
height-balanced
.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            """
            return tuple: depth from root and bool 'balanced' answer
            """
            if not root:
                return 0, True
            left, right = dfs(root.left), dfs(root.right)
            # depth from root and bool 'balanced'=compared 'depths' AND deeper nodes 'balanced'
            return max(left[0], right[0]) + 1, abs(left[0] - right[0]) <= 1 and left[1] and right[1]

        if not root:
            return True

        return dfs(root)[1]
