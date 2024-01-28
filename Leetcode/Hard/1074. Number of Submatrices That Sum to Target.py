"""
1074. Number of Submatrices That Sum to Target
(Hard complexity)

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'."""


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        for row in matrix:
            for col in range(cols - 1):
                row[col + 1] += row[col]

        ans = 0
        for cur in range(cols):
            for nxt in range(cur, cols):
                counts = defaultdict(int)
                cur_count, counts[0] = 0, 1
                for row in range(rows):
                    cur_count += matrix[row][nxt] - (matrix[row][cur - 1] if cur > 0 else 0)
                    ans += counts[cur_count - target]
                    counts[cur_count] += 1

        return ans