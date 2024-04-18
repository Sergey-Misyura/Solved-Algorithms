"""
463. Island Perimeter
(Easy complexity)

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])  # строки, столбцы
        answer = 0  # ответ
        shifts = ((-1, 0), (0, 1), (1, 0), (0, -1))  # сдвиги
        for i in range(rows): # проходим по строкам
            for j in range(cols): # проходим по столбцам
                if grid[i][j] == 1:  # если в клетке - остров
                    for dx, dy in shifts:  # проходим по сдвигам
                        if i + dx < 0 or i + dx >= rows or j + dy < 0 or j + dy >= cols or grid[i + dx][j + dy] == 0:  # если с островом вода - увеличиваем ответ
                            answer += 1
        # ответ
        return answer