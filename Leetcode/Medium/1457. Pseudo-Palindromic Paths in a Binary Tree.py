"""
1457. Pseudo-Palindromic Paths in a Binary Tree
(Medium complexity)

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, nums_set):
            if not node:
                return 0

            if node.val not in nums_set:
                nums_set.add(node.val)
            else:
                nums_set.remove(node.val)

            if not node.left and not node.right:
                return 1 if len(nums_set) <= 1 else 0

            return dfs(node.left, nums_set.copy()) + dfs(node.right, nums_set.copy())

        return dfs(root, set())