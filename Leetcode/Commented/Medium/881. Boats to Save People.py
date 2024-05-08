"""
881. Boats to Save People
(Medium complexity)

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  # сортируем массив людей
        answer = 0  # ответ
        lf, rg = 0, len(people) - 1  # левый, правый указатели
        while lf <= rg:  # пока указатели не сошлись
            answer += 1  # увеличиваем ответ
            if people[lf] + people[rg] <= limit:  # если в лодку можем добавить людей по левому указателю - двигаем левый
                lf += 1
            rg -= 1  # двигаем правый указатель
        # ответ
        return answer
