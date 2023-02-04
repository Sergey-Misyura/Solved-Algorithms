"""
350. Intersection of Two Arrays II
(Easy complexity)

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return 
the result in any order.
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result_list = []
        intersec = set(nums1).intersection(set(nums2))
      
        for i in intersec:
            for _ in range(min(nums1.count(i), nums2.count(i))):
                result_list.append(i)

        return result_list 