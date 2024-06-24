"""
1052. Grumpy Bookstore Owner
(Medium complexity)

There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.
"""


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(grumpy)  # число посещений
        ans = 0  # ответ
        for i in range(n):  # увеличиваем ответ при no grumpy
            if grumpy[i] == 0:
                ans += customers[i]
                customers[i] = 0
        
        max_ad, cur_ad = 0, 0  # максимально добавляемое значение, текущее оконное значение 
        for i, val in enumerate(customers):  # проходим по посетителям
            cur_ad += val  # двигаем правую границу
            if i >= minutes:  # двигаем левую границу
                cur_ad -= customers[i - minutes]
            max_ad = max(max_ad, cur_ad)  # обновляем max_ad
        
        # ответ
        return ans + max_ad




