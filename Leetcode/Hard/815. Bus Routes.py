"""
815. Bus Routes
(Hard complexity)

You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
"""


class Solution:
    def numBusesToDestination(self, routes, source, target):

        stops = collections.defaultdict(set) # in every stop list of routes
        for n, route in enumerate(routes):
            for stop in route:
                stops[stop].add(n)

        buses_count = 0
        bfs_list = [(source, buses_count)]
        seen_stops = set([source])

        for cur_stop, buses_count in bfs_list:
            if cur_stop == target:
                return buses_count
            for cur_route in stops[cur_stop]:
                for next_stop in routes[cur_route]:
                    if next_stop not in seen_stops:
                        bfs_list.append((next_stop, buses_count + 1))
                        seen_stops.add(next_stop)
                routes[cur_route] = []  # change seen route to []

        return -1
