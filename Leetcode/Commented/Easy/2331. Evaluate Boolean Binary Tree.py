"""
2331. Evaluate Boolean Binary Tree
(Easy complexity)

You are given the root of a full binary tree with the following properties:

Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left:  # если дошли до листа, 
            return root.val == 1  # возвращаем bool листа
        if root.val == 2:  # при значении узла 2 получаем OR из рекурсивно вызванной evaluateTree на потомках
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else:  # иначе получай AND из рекурсивно вызванной evaluateTree на потомках
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)