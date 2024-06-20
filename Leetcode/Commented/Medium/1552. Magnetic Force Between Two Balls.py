"""
1552. Magnetic Force Between Two Balls
(Medium complexity)

In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.
"""


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)  # длина position
        position.sort()  # сортируем

        def binSearchRight(lf, rg, check, checkparams):
            while lf < rg:  # ищем пока указатели не сошлись
                mid = (lf + rg + 1) // 2
                if check(mid, checkparams):
                    lf = mid
                else:
                    rg = mid - 1
            return lf


        def check_target(m, target):
            total, cur_val = 1, position[0]  # количество помещенных мячей, текущее значение
            for i in range(1, n):  # проходим по position
                if position[i] - cur_val >= m:  # когда нашли разницу больше m - ложим мяч, обновляем total, cur_val
                    total += 1
                    cur_val = position[i]
            return total >= target

        # левый бин поиск по ответу от 0 до макс разницы
        return binSearchRight(0, position[-1] - position[0], check_target, m)