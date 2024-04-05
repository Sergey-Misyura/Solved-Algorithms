"""
11. Container With Most Water
(Medium complexity)

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lf, rg = 0, len(height) - 1  # левая правая граница окна
        ans = 0  # ответ

        while lf < rg:  # пока границы не сошлись
            ans = max(ans, (rg - lf) * min(height[lf], height[rg]))  # обновляем ответ по объему в границах
            if height[lf] < height[rg]:  # если левая граница меньше правой
                lf += 1  # двигаем левую границу
            else:  # иначе двигаем правую границу
                rg -= 1
        # ответ
        return ans