"""
2485. Find the Pivot Integer
(Easy complexity)

Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:  # частный случай
            return 1
        else:
            all_sum = n * (n + 1)/2  # считаем общую сумму
            p = (n * 2) // 4  # считаем первое число для цикла проверки, начинается точно во второй половине чисел
            answer = -1  # переменная ответа
            cur_sum = (p - 1) * p / 2  # текущая сумма от 1 до p
            for num in range(p, n):  # проходим по числам от p до n - 1
                if cur_sum + num == all_sum - cur_sum:  # если текущая сумма + p равна сумме от p до n - сохраняем ответ
                    answer = num
                    break
                cur_sum += num  # увеличиваем cur_sum при переходе к следующему числу
            # ответ
            return answer
