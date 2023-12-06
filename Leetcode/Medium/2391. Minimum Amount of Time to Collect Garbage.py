"""
2391. Minimum Amount of Time to Collect Garbage

(Medium complexity)

You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.

Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.
"""

from itertools import accumulate


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        last = [0] * 3
        for i, types in enumerate(garbage):
            for type in types:
                last[ord(type) % 5] = i

        dist_acc = list(accumulate(travel, initial=0))

        total = sum((dist_acc[last[i]] for i in range(3)))
        total += sum(map(len, garbage))

        return total