"""
994. Rotting Oranges
(Medium complexity)

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        time, queue, next_queue = 0, [], []
        shifts = ((-1,0), (0, 1), (1,0), (0,-1))
        big_grid = [[0]*(cols+2)]
        for row in grid:
            big_grid.append([0]+row+[0])
        big_grid.append([0]*(cols+2))

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if big_grid[i][j]==2:
                    queue.append((i, j))

        while queue or next_queue:
            while queue:
                coords = queue.pop(0)
                curr_i, curr_j = coords[0], coords[1]

                for shift in shifts:
                    if big_grid[curr_i+shift[0]][curr_j+shift[1]]==1:
                        big_grid[curr_i+shift[0]][curr_j+shift[1]] = 2
                        next_queue.append((curr_i+shift[0], curr_j+shift[1]))
            time = time+1
            queue, next_queue = next_queue[:], []

        for row in big_grid:
            if 1 in row:
                return -1
        return 0 if time==0 else time-1
