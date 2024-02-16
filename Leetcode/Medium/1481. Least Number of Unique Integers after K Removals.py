"""
1481. Least Number of Unique Integers after K Removals
(Medium complexity)

Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
"""


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        count = Counter(arr)
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        while k > 0 and sorted_count:
            if k >= sorted_count[-1][1]:
                k -= sorted_count[-1][1]
                sorted_count.pop()
            else:
                k = 0
        return (len(sorted_count))