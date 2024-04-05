"""
1679. Max Number of K-Sum Pairs
(Medium complexity)

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0  # ответ
        count = defaultdict(int)  # счетчик чисел
        for num in nums:  # проходим по num
            if count[num] > 0:  # если число num есть в счетчике, увеличиваем ans, уменьшаем число num
                ans += 1
                count[num] -= 1
            else:  # иначе добавляем искомую разницу для вычеркивания
                count[k - num] += 1
        # ответ
        return ans