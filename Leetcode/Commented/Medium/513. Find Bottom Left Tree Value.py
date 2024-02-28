"""
513. Find Bottom Left Tree Value
(Medium complexity)

Given the root of a binary tree, return the leftmost value in the last row of the tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        def traverse(node):
            """
            Функция рекурсивного обхода дерева для поиска крайнего левого узла снизу
            :param node: текущий узел поддерева
            :return: высоту текущего узла и нижний крайний левый элемент его поддерева
            """
            # если нет узла - возвращаем -1, -1
            if not node:
                return -1, -1

            # обходим левое и правое поддеревья
            lf_height, lf_value = traverse(node.left)
            rg_height, rg_value = traverse(node.right)
            # если нет обоих поддеревьев - возвращаем значение текущего узла с высотой 1
            if lf_height == -1 and rg_height == -1:
                return 1, node.val
            # иначе, если левое поддерево глубже или на уровне правого - возвращаем высоту левого поддерева + 1
            # и левый крайний элемент из левого поддерева
            elif lf_height >= rg_height:
                return lf_height + 1, lf_value
            # если высота правого поддерева глубже - возвращаем высоту правого поддерева + 1 и
            # левый крайний элемент из правого поддерева
            else:
                return rg_height + 1, rg_value

        # ответ - нижний левый красний элемент дерева
        return traverse(root)[1]
