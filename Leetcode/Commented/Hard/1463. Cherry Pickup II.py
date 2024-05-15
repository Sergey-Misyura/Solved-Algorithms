"""
1463. Cherry Pickup II
(Hard complexity)

You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid.
"""


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])  # высота, ширина grid

        @lru_cache(None)  # кеширование
        def dfs(r, c1, c2):  # dfs для двух роботов - текущая строка, координаты робот1, робот2
            if r == m:  # когда дошли до конца - возвращаем 0
                return 0
            cherries = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]  # собранные на текущей строки вишни
            ans = 0  # макс число вишен собранных с нижних строк
            for nc1 in range(c1 - 1, c1 + 2):  # цикл вариантов обхода первого робота для следующей строки
                for nc2 in range(c2 - 1, c2 + 2):  # цикл вариантов обхода второго робота для следующей строки
                    if 0 <= nc1 < n and 0 <= nc2 < n:  # если не вышли за пределы массива
                        ans = max(ans, dfs(r + 1, nc1, nc2))  # обновляем ans, запуская dfs c следующей строки
            # возвращаем ans и вишни, собранные на текущей строке
            return ans + cherries
        # ответ
        return dfs(0, 0, n - 1)

