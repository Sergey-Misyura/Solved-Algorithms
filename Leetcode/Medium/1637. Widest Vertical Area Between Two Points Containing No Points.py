"""
1637. Widest Vertical Area Between Two Points Containing No Points
(Medium complexity)

Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.
"""


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        cur_max = 0
        points = sorted([x for x, _ in points])
        for i in range(1, len(points)):
            cur_max = max(cur_max, points[i] - points[i - 1])

        return cur_max