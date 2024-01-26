"""
576. Out of Boundary Paths
(Medium complexity)

There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
"""


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        @cache
        def pathsCount(row, col, moves):
            if row == m or row < 0 or col == n or col < 0:
                return 1
            if moves == 0:
                return 0

            count = 0
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                count = (count + pathsCount(row + dx, col + dy, moves - 1)) % (10 ** 9 + 7)

            return count

        return pathsCount(startRow, startColumn, maxMove) 