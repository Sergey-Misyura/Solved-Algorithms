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

        stack = [(p, q)]
        while stack:
            p_cur, q_cur = stack.pop()
            if p_cur and q_cur and p_cur.val == q_cur.val:
                stack.extend([(p_cur.left, q_cur.left), (p_cur.right, q_cur.right)])
            elif p_cur != q_cur:
                return False

        return True



