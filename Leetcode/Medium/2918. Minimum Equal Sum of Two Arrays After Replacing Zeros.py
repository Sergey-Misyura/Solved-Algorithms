"""
2918. Minimum Equal Sum of Two Arrays After Replacing Zeros
(Medium complexity)

You are given two arrays nums1 and nums2 consisting of positive integers.

You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.

Return the minimum equal sum you can obtain, or -1 if it is impossible.
"""


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        count1, count2 = nums1.count(0), nums2.count(0)

        if count1 == count2 == 0:
            return -1 if sum1 != sum2 else sum1
        elif count1 == 0:
            return -1 if sum1 <= sum2 or count2 > sum1 - sum2 else sum1
        elif count2 == 0:
            return -1 if sum2 <= sum1 or count1 > sum2 - sum1 else sum2
        else:
            return max(sum1 + count1, sum2 + count2)