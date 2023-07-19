"""
435. Non-overlapping Intervals

(Medium complexity)

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ln = len(intervals)

        prev, count = 0, 1

        for i in range (1, ln):
            if intervals[i][0]>= intervals[prev][1]:
                prev = i
                count += 1

        return ln - count