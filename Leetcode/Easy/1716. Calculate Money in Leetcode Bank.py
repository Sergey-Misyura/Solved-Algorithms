"""
1716. Calculate Money in Leetcode Bank
(Medium complexity)

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
"""

class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, 7)
        total = 0
        if weeks:
            total += 28 * weeks
            total += 7 * (weeks-1) * weeks/2
        if days :
            total += days * weeks
            total += days * (days + 1)/2

        return int(total)