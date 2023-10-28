"""
515. Find Largest Value in Each Tree Row
(Easy complexity)

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        vals = set()
        ans = []
        while queue:
            row = []
            new_queue = []
            for node in queue:
                if node:
                    row.append(node.val)
                    new_queue.append(node.left)
                    new_queue.append(node.right)
            if row:
                ans.append(max(row))
            queue = new_queue

        return ans