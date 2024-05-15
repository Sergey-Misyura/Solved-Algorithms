"""
200. Number of Islands
(Medium complexity)

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count, explored, rows, cols = 0, set(), len(grid), len(grid[0])  # число островов
        shifts = ((0, -1), (-1, 0), (0, 1), (1, 0))  # сдвиги

        def explore(x, y):  # функция поиска границ острова
            for shift in shifts:  # проходим по массиву сдвигов
                x_shifted, y_shifted = x + shift[0], y + shift[1]  # соседняя клетка
                # если сосед в границах поля, неизучен и земля
                if rows > x_shifted >= 0 and cols > y_shifted >= 0 and grid[x_shifted][y_shifted] == '1' \
                        and (x_shifted, y_shifted) not in explored:
                    explored.add((x_shifted, y_shifted))  # добавляем в explored
                    explore(x_shifted, y_shifted)  # вызываем рекурсивно explore от соседа

        for i in range(rows):  # проходим по строкам grid
            for j in range(cols):  # проходим по столбцам grid
                if grid[i][j] == '1' and (i, j) not in explored:  # если найдена земля и не изучена
                    count += 1  # увеличиваем количество островов
                    explored.add((i, j))  # добавляем в explored
                    explore(i, j)  # запускаем функцию поиска границ острова
        # ответ
        return count