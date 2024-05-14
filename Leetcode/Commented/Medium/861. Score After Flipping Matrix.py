"""
861. Score After Flipping Matrix
(Medium complexity)

You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).
"""


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])  # высота, ширина grid
        ans = (1 << (m - 1)) * n  # ответ, начальные значение - в 1 столбце все 1, отстальное 0

        for j in range(1, m):  # проходим по столбцам
            cur = 1 << (m - 1 - j)  # 1 в текущем столбце, остальное 0
            cnt = 0  # количество повторений
            for i in range(n):  # проходим по строке в столбце
                cnt += 1 if grid[i][j] == grid[i][0] else 0  # если соответствует первому в столбце, то cnt + 1

            ans += max(cnt, n - cnt) * cur  # увеличиваем ответ на большее из cnt и n - cnt умноженное на cur
        # ответ
        return ans