"""
210. Course Schedule II
(Medium complexity)

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        from collections import defaultdict
        courses = defaultdict(list)

        for a, b in prerequisites:
            courses[a].append(b)

        ans, vis = [], [0] * numCourses

        def dfs(cour, ans):
            if vis[cour]:
                return vis[cour] == 1, ans
            vis[cour] = -1
            if any(not dfs(b, ans)[0] for b in courses[cour]):
                return False, ans
            vis[cour] = 1
            ans.append(cour)
            return True, ans

        for cour in range(numCourses):
            ans = dfs(cour, ans)[1]

        return ans * (len(ans) == numCourses)
