"""
623. Add One Row to Tree
(Medium complexity)

Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:  # если глубина 1 - добавляем узел, делаем корень левым его потомком
            return TreeNode(val, root, None)

        nodes_deque = deque([root])  # дек узлов в bfs
        while nodes_deque and depth != 1:  # проходим по дереву пока не дошли до нужной глубины
            cur_breadth = len(nodes_deque)  # длина узлов на текущем уровне
            depth -= 1
            for _ in range(cur_breadth):  # проходим по текущему уровню
                cur = nodes_deque.popleft()
                if cur.left != None:  # добавляем левого потомка в дек
                    nodes_deque.append(cur.left)
                if cur.right != None:  # добавляем правого потомка в дек
                    nodes_deque.append(cur.right)

                if depth == 1:  # когда находимся на нужном уровене - вставляем узел
                    cur.left = TreeNode(val, cur.left, None)
                    cur.right = TreeNode(val, None, cur.right)
        # ответ
        return root