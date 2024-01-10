"""
2385. Amount of Time for Binary Tree to Be Infected
(Medium complexity)

You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        def traverse(node):
            if not node:
                return -1, 0, 0, False

            lf_max_len, lf_inf_len, lf_steps_to, lf_infected = traverse(node.left)
            rg_max_len, rg_inf_len, rg_steps_to, rg_infected = traverse(node.right)

            steps_to, infected = 0, False
            inf_len = max(lf_inf_len, rg_inf_len)
            if lf_infected:
                steps_to = lf_steps_to + 1
                max_len = max(lf_max_len, rg_max_len + 1 + steps_to)
                infected = True
            elif rg_infected:
                steps_to = rg_steps_to + 1
                max_len = max(rg_max_len, lf_max_len + 1 + steps_to)
                infected = True
            else:
                max_len = max(lf_max_len, rg_max_len) + 1

            if node.val == start:
                inf_len = max(lf_max_len, rg_max_len) + 1
                max_len = inf_len
                infected = True

            return max_len, inf_len, steps_to, infected

        max_len, inf_len, _, _ = traverse(root)
        return max(max_len, inf_len)



