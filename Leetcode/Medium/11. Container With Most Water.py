"""
11. Container With Most Water
(Medium complexity)

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lf, rg = 0, len(height) - 1
        ans = 0

        while lf < rg:
            ans = max(ans, (rg - lf) * min(height[lf], height[rg]))
            if height[lf] < height[rg]:
                lf += 1
            else:
                rg -= 1

        return ans