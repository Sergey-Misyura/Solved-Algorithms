"""
2373. Largest Local Values in a Matrix
(Easy complexity)

You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.
"""


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)  # высота поля
        answer = [[0] * (n - 2) for _ in range(n - 2)]  # матрица ответа
        shifts = ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1))  # сдвиги
        for i in range(1, n - 1):  # проходим по строкам grid
            for j in range(1, n - 1):  # проходим по столбцам grid
                answer[i - 1][j - 1] = max([grid[i + dy][j + dx] for dy, dx in shifts])  # в ответ записываем max из сосдних ячеек
        # ответ
        return answer