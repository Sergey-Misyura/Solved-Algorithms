"""
605. Can Place Flowers
(Easy complexity)

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # текущее число посаженных цветов
        flowerbed = [0] + flowerbed + [0]  # добавляем границы для flowerbed
        for i in range(1, len(flowerbed) - 1):   # проходим по flowerbed
            if flowerbed[i] == 0:  # если нашли пустое место
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:  # и если нет соседей
                    flowerbed[i] = 1  # сажаем цветок
                    count += 1  # увеличиваем счетчик count
        # ответ
        return count >= n