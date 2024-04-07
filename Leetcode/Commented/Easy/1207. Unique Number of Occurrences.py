"""
1207. Unique Number of Occurrences
(Easy complexity)

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)  # счетчик числа повторений чисел в arr
        # ответ - число уникальных чисел == числу уникальных повторений
        return len(counts) == len(set(counts.values()))