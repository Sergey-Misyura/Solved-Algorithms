"""
129. Sum Root to Leaf Numbers
(Medium complexity)

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

leaf node is a node with no children.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def traverse(node, cur_sum):  # функция обхода дерева
            if not node.left and not node.right:  # когда дошли до листа возвращаем число
                return cur_sum * 10 + node.val
            res = 0  # результат
            if node.right:  # если есть правый потомок - рекурсивно уходим в него, увеличивая число
                res += traverse(node.right, cur_sum * 10 + node.val)
            if node.left:  # если есть левый потомок - рекурсивно уходим в него, увеличивая число
                res += traverse(node.left, cur_sum * 10 + node.val)
            # возвращаем полученный от потомков ответ
            return res
        # ответ
        return traverse(root, 0)