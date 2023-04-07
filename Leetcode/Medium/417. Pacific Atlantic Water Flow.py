"""
417. Pacific Atlantic Water Flow
(Medium complexity)

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        pac = [(i, 0) for i in range(rows)] + [(0, i) for i in range(1, cols)]
        ath = [(i, cols - 1) for i in range(rows)] + [(rows - 1, i) for i in range(cols - 1)]

        def bfs(cells):
            dq = collections.deque(cells)
            vis = set(cells)
            while dq:
                i, j = dq.popleft()
                for n_i, n_j in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                    if rows > n_i >= 0 and cols > n_j >= 0 and heights[n_i][n_j] >= heights[i][j] \
                            and (n_i, n_j) not in vis:
                        dq.append((n_i, n_j))
                        vis.add((n_i, n_j))

            return vis

        return bfs(pac) & bfs(ath)
