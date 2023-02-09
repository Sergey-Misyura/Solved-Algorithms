"""
200. Number of Islands
(Medium complexity)

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid: return 0
        count, explored, rows, cols = 0, set(), len(grid), len(grid[0])
        shifts = ((0,-1), (-1,0), (0,1), (1,0))

        def exploreIsland(x, y):
            for shift in shifts:
                x_shifted,  y_shifted = x+shift[0], y+shift[1]
                if rows>x_shifted>=0 and cols>y_shifted>=0 and grid[x_shifted][y_shifted]=='1' \
                    and (x_shifted, y_shifted) not in explored:
                        explored.add((x_shifted,y_shifted))
                        exploreIsland(x_shifted, y_shifted)

        for i in range(rows):
            for j in range(cols):

                if grid[i][j]=='1' and (i, j) not in explored:
                    count+=1
                    explored.add((i,j))
                    exploreIsland(i,j)
                    

        return count
