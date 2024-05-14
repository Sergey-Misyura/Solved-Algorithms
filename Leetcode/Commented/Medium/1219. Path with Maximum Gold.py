"""
1219. Path with Maximum Gold
(Medium complexity)

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
"""


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        shifts = ((-1, 0), (0, 1), (1, 0), (0, -1))  # массив сдвигов
        n, m = len(grid), len(grid[0])  # высота, ширина grid

        def rec(row, col, visited, cur_val):  # рекурсивная функция подсчета max монет из текущей ячейки с предыдущим значением монет
            if row < 0 or row > n - 1 or col < 0 or col > m - 1 or grid[row][col] == 0:  # если вышли за grid - возвращаем cur_val
                return cur_val
            cur_val += grid[row][col]  # увеличиваем cur_val на значение текущей ячейки
            visited.add((row, col))  # добавляем текущую ячейку в посещенные
            gold = cur_val  # возвращаемое значение
            for di, dj in shifts:  # проходим по сдвигам
                if (row + di, col + dj) not in visited:  # если новая ячейка не в visited
                    gold = max(gold, rec(row + di, col + dj, visited.copy(), cur_val))  # обновляем gold, вызывая rec в новой ячейке grid
            return gold

        answer = 0  # ответ
        for i in range(n):  # проходим по grid вызывая rec
            for j in range(m):
                answer = max(answer, rec(i, j, set(), 0))  # обновляем answer
        # ответ
        return answer
