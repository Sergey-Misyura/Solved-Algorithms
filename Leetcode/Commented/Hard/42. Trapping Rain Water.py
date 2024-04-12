"""
42. Trapping Rain Water
(Hard complexity)

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)  # длина карты высот
        ans = 0   # ответ

        cur_trap, cur_max = 0, height[0]  # накопление воды, текущий максимум
        for i in range(1, n):  # проходим по массиву слева направо
            if height[i] >= cur_max:  # если высота выше текущего максимума
                ans += cur_trap  # добавляем в ответ накопленную воду
                cur_max, cur_trap = height[i], 0  # обновляем текущий максимум, накопление воды
            else:  # иначе увеличиваем накопление воды
                cur_trap += cur_max - height[i]

        cur_trap, cur_max = 0, height[-1]  # накопление воды, текущий максимум
        for i in range(n-2, -1, -1):  # проходим по массиву справа налево, выполняя теже действия
            if height[i] > cur_max:
                ans += cur_trap
                cur_max, cur_trap = height[i], 0
            else:
                cur_trap += cur_max - height[i]
        # ответ
        return ans