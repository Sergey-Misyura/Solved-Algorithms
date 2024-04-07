"""
2352. Equal Row and Column Pairs
(Medium complexity)

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count_grid = Counter(map(tuple, grid))  # счетчик повторений строк в grid
        cont_trans_grid = Counter(zip(*grid))  # счетчик повторений столбцов в grid
        answer = 0  # ответ
        for key in count_grid:  # для каждой строки в count_grid
            if key in cont_trans_grid:  # если строка есть в столбцах
                answer += count_grid[key] * cont_trans_grid[key]  # увеличиваем answer
        # ответ
        return answer
