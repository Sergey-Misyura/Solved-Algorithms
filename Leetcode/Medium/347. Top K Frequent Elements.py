"""
347. Top K Frequent Elements

(Medium complexity)

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        return [i[0] for i in count.most_common(k)]



