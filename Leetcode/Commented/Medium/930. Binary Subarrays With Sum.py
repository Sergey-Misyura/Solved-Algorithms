"""
930. Binary Subarrays With Sum
(Medium complexity)

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.
"""


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_count = 0  # число подмассивов с суммой goal
        pref_sum = 0  # преф сумма
        sum_counter = {0: 1}  # счетчик сумм в подмассиве

        for num in nums:  # проходим по nums
            pref_sum += num  # увеличиваем преф сумму
            if pref_sum - goal in sum_counter:  # если уже встречали pref_sum - goal, то есть сумма на подмассиве равна goal
                total_count += sum_counter[pref_sum - goal]  # увеличиваем total_count на количество подмассивов с суммой goal
            sum_counter[pref_sum] = sum_counter.get(pref_sum, 0) + 1  # увеличиваем счетчик преф сумм в sum_counter
        # ответ
        return total_count
