"""
1442. Count Triplets That Can Form Two Arrays of Equal XOR
(Medium complexity)

Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.
"""


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        xor_arr = [0] + [arr[0]]  # преф xor
        for i in range(1, n):
            xor_arr.append(xor_arr[-1] ^ arr[i])

        n = len(xor_arr)
        answer = 0
        for i in range(n):  # проходим по массиву
            for j in range(i + 1, n):  # проходим от i + 1
                if xor_arr[j] - xor_arr[i] == 0:  # если нашли разницу по xor = 0 - увеличиваем ответ на длину между i j
                    answer += j - i - 1
        # ответ
        return answer
        