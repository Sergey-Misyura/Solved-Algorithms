"""
2997. Minimum Number of Operations to Make Array XOR Equal to K
(Medium complexity)

You are given a 0-indexed integer array nums and a positive integer k.

You can apply the following operation on the array any number of times:

Choose any element of the array and flip a bit in its binary representation. Flipping a bit means changing a 0 to 1 or vice versa.
Return the minimum number of operations required to make the bitwise XOR of all elements of the final array equal to k.

Note that you can flip leading zero bits in the binary representation of elements. For example, for the number (101)2 you can flip the fourth bit and obtain (1101)2.
"""


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0  # общий xor
        for num in nums:  # определяем xor для всех nums
            xor = xor ^ num

        total = 0  # мин число операций
        while k or xor:  # пока есть k или xor
            if (k % 2) != (xor % 2):  # если крайние правые биты не равны увеличиваем total
                total += 1
            # сдвиг для удаления крайних правых бит
            k //= 2
            xor //= 2
        # ответ
        return total
