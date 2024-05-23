"""
979. Distribute Coins in Binary Tree
(Medium complexity)

You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0  # число ходов
        def dfs(node):  # рекурсивный поиск в глубину
            if not node:  # если нет узла - обменивать монеты не нужно
                return 0
            left = dfs(node.left)  # число обменов слева
            right = dfs(node.right)  # число обменов справа
            self.moves += abs(left) + abs(right)  # увеличиваем итоговое число ходов на количество монет для обмена с родительским узлом
            return node.val - 1 + left + right # возвращаем число ходов для узла
        dfs(root)
        # ответ
        return self.moves
