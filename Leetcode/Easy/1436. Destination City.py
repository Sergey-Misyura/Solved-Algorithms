"""
1436. Destination City
(Easy complexity)

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
"""

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from_ = set(path[0] for path in paths)
        for path in paths:
            if path[1] not in from_:
                return path[1]