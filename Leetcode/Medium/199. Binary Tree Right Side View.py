"""
199. Binary Tree Right Side View
(Medium complexity)

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        output = []
        if root:
            level = [root]
            while level:
                output.append(level[-1].val)
                level = [lf_rg for node in level for lf_rg in (node.left, node.right) if lf_rg]
        return output
