"""
992. Subarrays with K Different Integers
(Hard complexity)

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.
"""


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # получаем число подмассивов с ровно k разными числами как разница между
        # число подмассивов с не более k разными числами и число подмассивов с не более k - 1 разными числами
        return self.at_most_k(nums, k) - self.at_most_k(nums, k - 1)

    def at_most_k(self, nums, k):  # функция подсчета подмассивов с не более k разных чисел
        answer = 0  # ответ
        count = [0] * (len(nums) + 1)  # массив-счетчик количества чисел

        lf = 0  # левая граница раздвижного окна
        for rg in range(len(nums)):  # проходим правой границей окна по nums
            count[nums[rg]] += 1  # увеличиваем счетчик числа nums[rg]
            if count[nums[rg]] == 1:  # когда впервые встретили число уменьшаем k
                k -= 1
            while k == -1:  # пока превышаем k разных чисел
                count[nums[lf]] -= 1  # уменьшаем счетчик числа nums[lf]
                if count[nums[lf]] == 0:  # когда количество чисел nums[lf] стало 0, увеличиваем k
                    k += 1
                lf += 1  # сдвигаем левую границу
            answer += rg - lf + 1  # к ответу прибавляем число подмассивов между lf и rg
        # ответ
        return answer

