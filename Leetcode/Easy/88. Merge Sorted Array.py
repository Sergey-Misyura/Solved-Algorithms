"""
88. Merge Sorted Array
(Easy complexity)
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur_m, cur_n, cur_res = m - 1, n - 1, m + n - 1
        while cur_n > -1:
            if cur_m > -1 and nums1[cur_m] > nums2[cur_n]:
                nums1[cur_res] = nums1[cur_m]
                cur_m -= 1
            else:
                nums1[cur_res] = nums2[cur_n]
                cur_n -= 1
            cur_res -= 1