"""
1289. Minimum Falling Path Sum II
(Hard complexity)

Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.
"""


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)  # количество строк в grid
        cur_row = grid[0]  # строка мин сумм путей для строк по i-ую
        for row in range(1, n):  # проходим по строкам
            next_row = [0] * n  # следующая строка сумм
            pref_min, suf_min = cur_row.copy(), cur_row.copy()  # преф и суф минимумы текущей суммы путей строк
            for i in range(1, n):  # считаем преф мин
                pref_min[i] = min(cur_row[i], pref_min[i - 1])
            for i in range(n - 2, -1, -1):  # считаем суф мин
                suf_min[i] = min(cur_row[i], suf_min[i + 1])
            next_row[0] = grid[row][0] + suf_min[1]  # начальное значение следующей строки
            for i in range(1, n - 1):  # считаем next_row из grid[row][i] и преф, суф сумм
                next_row[i] = grid[row][i] + min(pref_min[i - 1], suf_min[i + 1])
            next_row[n - 1] = grid[row][n - 1] + pref_min[n - 2]  # последней значение в следующей строке
            cur_row = next_row  # делаем next_row текущей
        # ответ - мин сумма пути
        return min(cur_row)

