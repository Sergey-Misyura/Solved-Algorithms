"""
84. Largest Rectangle in Histogram
(Hard complexity)

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0

        for i, cur_h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= cur_h:
                h = heights[stack.pop()]
                w = i
                if stack:
                    w = i - stack[-1] - 1

                ans = max(ans, h * w)
            stack.append(i)
        return ans