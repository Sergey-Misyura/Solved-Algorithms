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
        self.answer = 0  # переменная ответа

        # рекурсивная функция измерения глубины
        def depth_tree(node):
            # нет узла - глубина 0
            if not node:
                return 0
            # считаем глубины левого и правого поддеревьев
            lf, rg = depth_tree(node.left), depth_tree(node.right)
            # обновляем ответ если при обходе поддеревьев дерева получили больший радиус
            self.answer = max(self.answer, lf + rg)
            # возвращаем глубину дерева, на основе его поддеревьев
            return max(lf, rg) + 1

        # обход
        depth_tree(root)
        # ответ
        return self.answer