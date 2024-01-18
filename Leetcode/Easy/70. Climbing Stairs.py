"""
70. Climbing Stairs
(Easy complexity)

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        prev = cur = 1
        for _ in range(n-1):
            cur, prev = cur + prev, cur
        return cur