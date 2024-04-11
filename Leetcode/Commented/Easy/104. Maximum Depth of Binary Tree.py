"""
104. Maximum Depth of Binary Tree
(Easy complexity)

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(node):  # функция обхода дерева
            if not node:  # если нет узла - глубина 0
                return 0
            return max(traverse(node.left), traverse(node.right)) + 1  # возвращаем макс глубину + текущий узел
        # ответ
        return traverse(root)