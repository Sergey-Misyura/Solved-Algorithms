"""
589. N-ary Tree Preorder Traversal
(Easy complexity)

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. 
Each group of children is separated by the null value (See examples)
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root: return []

        nodes,branch = [], []
        branch.append(root)

        while branch:
            node = branch.pop()
            nodes.append(node.val)

            for child in node.children[::-1]:
                branch.append(child)
        
        return nodes