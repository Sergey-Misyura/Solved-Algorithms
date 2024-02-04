"""
1043. Partition Array for Maximum Sum
(Medium complexity)

Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            cur_max = 0
            for kk in range(1, min(k, i) + 1):
                cur_max = max(cur_max, arr[i - kk])
                dp[i] = max(dp[i], dp[i - kk] + cur_max * kk)

        return dp[n]