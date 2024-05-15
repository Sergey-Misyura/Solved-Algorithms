"""
1992. Find All Groups of Farmland
(Medium complexity)

You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].

Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.
"""


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n, m = len(land), len(land[0])  # высота, ширина land
        answer = []  # массив ответа

        for i in range(n):  # проходим по строкам
            for j in range(m):  # проходим по столбцам
                if land[i][j] == 1 and (i == 0 or land[i - 1][j] == 0) and (j == 0 or land[i][j - 1] == 0):  # находим левый верхний угол
                    bot_row = i
                    rg_col = j
                    while bot_row + 1 < n and land[bot_row + 1][j] == 1:  # двигаемся вниз по строкам пока есть farmland
                        bot_row += 1
                    while rg_col + 1 < m and land[i][rg_col + 1] == 1:  # двигаемся вправо по столбцам пока есть farmland
                        rg_col += 1

                    answer.append([i, j, bot_row, rg_col])  # добавляем в ответ левый верхний и правый нижний углы
        # ответ
        return answer