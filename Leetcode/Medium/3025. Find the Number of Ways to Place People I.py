"""
3025. Find the Number of Ways to Place People I
(Medium complexity)

You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

We define the right direction as positive x-axis (increasing x-coordinate) and the left direction as negative x-axis (decreasing x-coordinate). Similarly, we define the up direction as positive y-axis (increasing y-coordinate) and the down direction as negative y-axis (decreasing y-coordinate)

You have to place n people, including Chisato and Takina, at these points such that there is exactly one person at every point. Chisato wants to be alone with Takina, so Chisato will build a rectangular fence with Chisato's position as the upper left corner and Takina's position as the lower right corner of the fence (Note that the fence might not enclose any area, i.e. it can be a line). If any person other than Chisato and Takina is either inside the fence or on the fence, Chisato will be sad.

Return the number of pairs of points where you can place Chisato and Takina, such that Chisato does not become sad on building the fence.

Note that Chisato can only build a fence with Chisato's position as the upper left corner, and Takina's position as the lower right corner. For example, Chisato cannot build either of the fences in the picture below with four corners (1, 1), (1, 3), (3, 1), and (3, 3), because:

With Chisato at (3, 3) and Takina at (1, 1), Chisato's position is not the upper left corner and Takina's position is not the lower right corner of the fence.
With Chisato at (1, 3) and Takina at (1, 1), Takina's position is not the lower right corner of the fence.
"""


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        points += [[float('-inf'), float('inf')]]

        total = 0
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            m = -inf
            for j in range(i + 1, len(points)):
                x_second = points[j][0]
                y_second = points[j][1]
                if y_second > m and y_second <= y:
                    m = y_second
                    total += 1

        return total



