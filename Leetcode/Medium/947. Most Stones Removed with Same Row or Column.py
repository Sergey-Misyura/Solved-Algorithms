"""
947. Most Stones Removed with Same Row or Column
(Medium complexity)

On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.
"""


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        graph = {}

        def search(stone):

            if stone != graph.setdefault(stone, stone):
                graph[stone] = search(graph[stone])

            return graph[stone]

        for i, j in stones:
            graph[search(i)] = search(~j)

        return len(stones) - len({search(x) for x in graph})
