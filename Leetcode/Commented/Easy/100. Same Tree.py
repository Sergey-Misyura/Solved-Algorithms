"""
100. Same Tree
(Easy complexity)

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # если есть оба узла
        if p and q:
            # рекурсивно проверяем на рпвенство значения узлов обих деревьев, левые и правые поддеревья
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # условие сравнения концов поддеревьев: если есть 1 из узлов - False, оба узла в None None - True
        return p is q