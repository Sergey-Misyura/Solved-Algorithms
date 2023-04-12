"""
547. Number of Provinces
(Medium complexity)

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        count, visited, con_count = len(isConnected), set(), 0

        def dfs(city):

            for idx, con in enumerate(isConnected[city]):

                if (idx not in visited) and (con == 1):
                    visited.add(idx)
                    dfs(idx)

        for city in range(count):

            if city not in visited:
                dfs(city)
                con_count += 1

        return con_count
        