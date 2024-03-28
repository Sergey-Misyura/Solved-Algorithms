"""
2958. Length of Longest Subarray With at Most K Frequency
(Medium complexity)

You are given an integer array nums and an integer k.

frequency of an element x is the number of times it occurs in an array.

An array is called good if the frequency of each element in this array is less than or equal k.

Return the length of the longest good subarray of nums.

subarray is a contiguous non-empty sequence of elements within an array.
"""


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)  # счетчик повторений чисел
        lf = 0  # левая граница раздвижного окна
        answer = 0  # переменная ответа
        for rg in range(len(nums)):  # проходим правой границей раздвижного окна по nums
            counts[nums[rg]] += 1  # увеличиваем счетчик в counts
            if counts[nums[rg]] > k:  # если число повторений текущего числа > k
                while nums[lf] != nums[rg]:  # двигаем левую границу пока не встретим такое же число как nums[rg]
                    counts[nums[lf]] -= 1  # уменьшаем счетчик
                    lf += 1
                counts[nums[lf]] -= 1 # сдвигаем lf еще на 1
                lf += 1
            answer = max(answer, rg - lf + 1)  # обновляем длину последовательности в answer

        # ответ
        return answer
