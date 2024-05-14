"""
151. Reverse Words in a String
(Medium complexity)

You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].
"""


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []  # heap
        n = len(arr)  # длина массива
        for i in range(n - 1):  # проходим по массиву кроме последнего - добавляем в heap отношение текущий/последний
            heappush(heap, (arr[i]/arr[-1], i, n - 1))
        for _ in range(k):  # проходим до k
            _, num, denom = heappop(heap)  # достаем из heap
            heappush(heap, (arr[num]/arr[denom-1], num, denom - 1))  # добавляем в heap число с тем же числителем, но сдвигаем знаменатель на 1 влево по arr
        # ответ - последний полученный из heap
        return [arr[num], arr[denom]]
