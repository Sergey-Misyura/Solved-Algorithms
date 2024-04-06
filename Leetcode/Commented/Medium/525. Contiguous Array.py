"""
525. Contiguous Array
(Medium complexity)

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = {0: -1}  # словарь количества 0 и 1 вида: количество: индекс
        answer = cur_count = 0  # ответ, текущее количество
        for i in range(len(nums)):  # проходим по nums
            cur_count += 1 if nums[i] == 1 else -1  # изменяем количество в зависимости от 0 и 1
            if cur_count in counts:  # если уже было cur_count, значит разница 0 и 1 между предыдущим индексом с cur_count и текущим равно 0, обновляем ответ
                answer = max(answer, i - counts[cur_count])
            else:  # иначе добавляем cur_count в counts
                counts[cur_count] = i
        # ответ
        return answer