"""
56. Merge Intervals
(Medium complexity)

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input."""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = []
        cur = intervals[0]
        for inter in intervals[1:]:
            if inter[0] <= cur[-1]:
                cur = [cur[0], max(cur[-1], inter[-1])]
            else:
                ans.append(cur)
                cur = inter
        ans.append(cur)

        return ans