"""
2265. Count Nodes Equal to Average of Subtree
(Medium complexity)

Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if not node:
                return 0, 0, 0

            lf_sum, lf_count, lf_res = traverse(node.left)
            rg_sum, rg_count, rg_res = traverse(node.right)

            node_sum = node.val + lf_sum + rg_sum
            node_count = 1 + lf_count + rg_count

            node_res = lf_res + rg_res
            if node_sum // node_count == node.val:
                node_res += 1
            return node_sum, node_count, node_res

        return traverse(root)[2]

