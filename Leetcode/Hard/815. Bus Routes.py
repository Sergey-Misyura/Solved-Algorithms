"""
417. Pacific Atlantic Water Flow
(Medium complexity)

You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
"""


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(set)
        for route, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(route)

        cur_routes, visited, count = graph[source], set(), 0

        while cur_routes:
            next_routes = set()

            for route in cur_routes:
                visited.add(route)
                for stop in routes[route]:
                    if stop == target:
                        return count + 1
                    for next_route in graph[stop] - visited:
                        next_routes.add(next_route)

            cur_routes = next_routes
            count += 1
        return -1
