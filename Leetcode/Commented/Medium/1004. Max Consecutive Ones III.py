"""
1004. Max Consecutive Ones III
(Medium complexity)

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lf = 0  # левая граница окна
        answer = 0  # ответ
        for rg in range(len(nums)):  # проходим правой границей по nums
            if nums[rg] == 0:  # если нашли 0, уменьшаем k
                k -= 1
            if k == 0:  # обновляем ответ при k = 0
                answer = max(answer, rg - lf + 1)
            while lf < rg and k < 0:  # если встретили 0 больше чем k раз, перемещаем левую границу окна
                if nums[lf] == 0:
                    k += 1
                lf += 1
        if k >= 0:  # доп проверка при возможных заменах k
            answer = max(answer, rg - lf + 1)
        # ответ
        return answer