"""
606. Construct String from Binary Tree
(Easy complexity)

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def traverse(node):
            if node == None:
                return ""
            output = str(node.val)
            left = traverse(node.left)
            right = traverse(node.right)
            if left or right:
                output += '(' + left + ')'
                if right:
                    output += '(' + str(right) + ')'
            return output

        return traverse(root)