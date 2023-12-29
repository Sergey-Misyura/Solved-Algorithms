"""
1335. Minimum Difficulty of a Job Schedule
(Hard complexity)

You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
"""


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1

        @cache
        def search_min(i, d):
            if d == 1:
                return max(jobDifficulty[i:])
            res, maxd = float('inf'), 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, jobDifficulty[j])
                res = min(res, maxd + search_min(j + 1, d - 1))
            return res
        return search_min(0, d)