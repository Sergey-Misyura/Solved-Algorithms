"""
85. Maximal Rectangle
(Hard complexity)

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
"""


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        answer = 0  # ответ
        heights = [0] * (len(matrix[0]) + 1)  # массив высот

        for row in matrix:  # проходим по строкам матрицы
            for col in range(len(matrix[0])):  # пересчитываем высоту
                heights[col] = heights[col] + 1 if row[col] == '1' else 0

            stack = []  # стек
            for col in range(len(heights)):  # проходим по колонкам в строке
                while stack and heights[col] < heights[stack[-1]]:  # пока текущая высота меньше высоты в стеке
                    height = heights[stack.pop()]  # получаем высоту
                    width = col if not stack else col - stack[-1] - 1  # считаем ширину
                    answer = max(answer, height * width)  # обновляем ответ
                stack.append(col)  # добавляем колонку в стек
        # ответ
        return answer