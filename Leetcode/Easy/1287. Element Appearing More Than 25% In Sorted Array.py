"""
1287. Element Appearing More Than 25% In Sorted Array
(Easy complexity)

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
"""

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return Counter(arr).most_common(1)[0][0]