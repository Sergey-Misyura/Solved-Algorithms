"""
2870. Minimum Number of Operations to Make Array Empty
(Medium complexity)

You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

Choose two elements with equal values and delete them from the array.
Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0

        for count in Counter(nums).values():
            if count == 1:
                return -1
            else:
                quot, rem = divmod(count, 3)
                if rem:
                    ans += 1
                ans += quot

        return ans


