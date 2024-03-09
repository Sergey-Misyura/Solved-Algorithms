"""
3005. Count Elements With Maximum Frequency
(Easy complexity)

You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.
"""


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count_dict = Counter(nums)  # счетчик частот элементов
        max_count = count_dict.most_common(1)[0][1]  # самое частое появление элемента
        total_count = 0  # общее число самых частых появлений
        for _, value in count_dict.items():  # проходим по значениям
            if value == max_count:  # если значение максимально - увеличиваем total_count
                total_count += value
        # ответ
        return total_count
