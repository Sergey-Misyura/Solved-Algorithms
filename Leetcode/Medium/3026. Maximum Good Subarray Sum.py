"""
3026. Maximum Good Subarray Sum
(Medium complexity)

You are given an array nums of length n and a positive integer k.

A subarray of nums is called good if the absolute difference between its first and last element is exactly k, in other words, the subarray nums[i..j] is good if |nums[i] - nums[j]| == k.

Return the maximum sum of a good subarray of nums. If there are no good subarrays, return 0.
"""


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        d = defaultdict(lambda: float('inf'))
        ans = float('-inf')
        for num in nums:
            cur_sum += num
            if d[num + k] != float('inf'):
                ans = max(ans, cur_sum - d[num + k])
            if d[num - k] != float('inf'):
                ans = max(ans, cur_sum - d[num - k])

            d[num] = min(d[num], cur_sum - num)

        return ans if ans != float('-inf') else 0
