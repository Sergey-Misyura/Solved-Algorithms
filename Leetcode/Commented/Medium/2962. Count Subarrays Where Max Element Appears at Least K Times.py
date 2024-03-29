"""
2962. Count Subarrays Where Max Element Appears at Least K Times
(Medium complexity)

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.
"""


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)  # длина nums
        max_num = max(nums)  # максимальное число в nums
        lf, rg, count, answer = 0, 0, 0, 0  # левый, правый указатели, число максимумом, ответ

        while rg < n:  # пока правая граница скользящего окна не вышла за nums
            if nums[rg] == max_num:  # увеличиваем счетчик count при max_num
                count += 1

            if count >= k:  # если нашли k повторений max_num
                while count >= k:  # пока количество повторений >= k проходим левой границей окна
                    # каждый раз увеличиваем ответ на разницу n - rg,
                    # так как каждое положение lf дает именно такое число подмассивов
                    answer += n - rg
                    if nums[lf] == max_num:  # уменьшаем счетчик
                        count -= 1
                    lf += 1

            rg += 1
        # ответ
        return answer
