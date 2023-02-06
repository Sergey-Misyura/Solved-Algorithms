"""
102. Binary Tree Level Order Traversal
(Medium complexity)

Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:return None
        answer, branches =[], [root]

        while branches:
            level = []

            for i in range(len(branches)):
                current_branch = branches.pop(0)
                level.append(current_branch.val)
                if current_branch.left!=None: branches.append(current_branch.left)
                if current_branch.right!=None: branches.append(current_branch.right)

            answer.append(level)
        
        return answer