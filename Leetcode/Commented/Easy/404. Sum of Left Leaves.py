"""
404. Sum of Left Leaves
(Easy complexity)

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverse(node, is_left):  # функция обхода дерева
            if not node:  # если нет узла - возвращаем 0
                return 0
            if not node.left and not node.right:  # если лист и он левый - возвращаем его значение, иначе 0
                return node.val if is_left else 0
            return traverse(node.left, True) + traverse(node.right, False)  # запускаем рекурсивно в потомках
        # ответ
        return traverse(root, False)
