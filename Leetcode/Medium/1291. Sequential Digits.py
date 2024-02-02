"""
1291. Sequential Digits
(Medium complexity)

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
"""


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        n, m = len(str(low)), len(str(high))
        ans = []
        for i in range(n, m + 1):

            cur = 1
            diff = 1
            for k in range(2, i + 1):
                cur = cur * 10 + k
                diff = diff * 10 + 1

            while cur < 10 ** i - 1 and cur <= high and cur % 10:
                if cur >= low:
                    ans.append(cur)
                cur += diff

        return ans

