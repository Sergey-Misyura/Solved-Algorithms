"""
1609. Even Odd Tree
(Medium complexity)

A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:  # если нет корня - ответ True
            return True
        queue = [root]  # создаем очередь из корня
        level = 0  # текущий уровень 0
        while queue:  # продолжаем пока есть очередь
            # предыдущее значение узла - -inf для четных, inf для нечетных
            prev = float('-inf') if level % 2 == 0 else float('inf')
            for _ in range(len(queue)):  # проходим по каждому уровню дерева
                node = queue.pop(0)  # достаем первый узел
                # если уровень четный и значение узла четное или <= предыдущего
                # либо уровень нечетный и значение узла нечетное или >= предыдущего - ответ False
                if (level % 2 == 0 and (node.val % 2 == 0 or node.val <= prev)) \
                        or (level % 2 != 0 and (node.val % 2 != 0 or node.val >= prev)):
                    return False
                if node.left:  # если есть левый узел - добавляем в очередь, формирует следующий уровень
                    queue.append(node.left)
                if node.right:  # если есть правый узел - добавляем в очередь, формирует следующий уровень
                    queue.append(node.right)
                prev = node.val  # обновляем предыдущее значение узла
            level += 1  # увеличиваем уровень
        # ответ
        return True
