"""
79. Word Search
(Medium complexity)

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, k, board):  # поиск в глубину
            if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1:  # проверка выхода за границы
                return False
            if board[i][j] != word[k] or k >= len(word):  # проверка соответствия ячейки букве слова
                return False

            if k == len(word) - 1:  # если не вышли раньше и прошли слово - ответ True
                return True

            shifts = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # массив сдвигов
            for di, dj in shifts:  # проходим по сдвигам
                sym = board[i][j]  # сохраняем текущее значение ячейки
                board[i][j] = '#'  # меняем на '#'

                if dfs(i + di, j + dj, k + 1, board):  # вызываем dfs в соседнюю клетку, если получили True, возвращаем True
                    return True

                board[i][j] = sym  # возвращаем на место символ в board


        # проходим по клеткам
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  # если в клетке начало слова - вызываем dfs
                    if dfs(i, j, 0, board):  # если успешно завершили dfs - ответ True
                        return True
        # если не нашли слово, ответ False
        return False




