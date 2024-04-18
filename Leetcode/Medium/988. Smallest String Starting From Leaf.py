"""
988. Smallest String Starting From Leaf
(Medium complexity)

You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, cur_str):  # обход в глубину
            if node:  # если в узле
                cur_str = chr(97 + node.val) + cur_str  # добавляем в начало текущей строки букву
                min_val = min(dfs(node.left, cur_str), dfs(node.right, cur_str))  # получаем минимум из детей
                if node.left == None and node.right == None:  # если в листе - возвращаем cur_str
                    min_val = cur_str
                # возвращаем мин строку
                return min_val
            # взвращаем знак больше чем 'z'
            return '{'
        # запускаем dfs от корня
        return dfs(root, '')