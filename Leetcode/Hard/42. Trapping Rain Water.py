"""
42. Trapping Rain Water
(Hard complexity)

Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0

        cur_trap, cur_max = 0, height[0]
        for i in range(1, n):
            if height[i] >= cur_max:
                ans += cur_trap
                cur_max, cur_trap = height[i], 0
            else:
                cur_trap += cur_max - height[i]

        cur_trap, cur_max = 0, height[-1]
        for i in range(n-2, -1, -1):
            if height[i] > cur_max:
                ans += cur_trap
                cur_max, cur_trap = height[i], 0
            else:
                cur_trap += cur_max - height[i]

        return ans