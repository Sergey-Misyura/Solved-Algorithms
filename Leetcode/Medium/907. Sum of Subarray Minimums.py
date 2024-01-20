"""
907. Sum of Subarray Minimums
(Medium complexity)

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        stack = []
        arr = [float('-inf')] + arr + [float('-inf')]
        for i, n in enumerate(arr):
            while stack and arr[stack[-1]] > n:
                cur = stack.pop()
                ans += arr[cur] * (i - cur) * (cur - stack[-1])
            stack.append(i)
        return ans % (10**9 + 7)
