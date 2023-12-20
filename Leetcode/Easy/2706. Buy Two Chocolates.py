"""
2706. Buy Two Chocolates
(Easy complexity)

You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.

You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.
"""

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min2 = float('inf')
        for price in prices:
            if price < min1:
                min2 = min1
                min1 = price
            elif price < min2:
                min2 = price

        return money-min1-min2 if money-min1-min2 > -1 else money
