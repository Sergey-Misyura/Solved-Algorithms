"""
2642. Design Graph With Shortest Path Calculator
(Hard complexity)

There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.

Implement the Graph class:

Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.
"""


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.edges = [[] for _ in range(n)]
        for from_, to_, cost in edges:
            self.edges[from_].append((to_, cost))

    def addEdge(self, edge: List[int]) -> None:
        from_, to_, cost = edge
        self.edges[from_].append((to_, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        n, heap = len(self.edges), [(0, node1)]
        dist = [inf] * n
        dist[node1] = 0

        while heap:
            total_dist, cur_node = heappop(heap)
            if cur_node == node2: return total_dist
            if dist[cur_node] <= total_dist:
                for neigh, cost in self.edges[cur_node]:
                    new_dist = total_dist + cost
                    if new_dist < dist[neigh]:
                        dist[neigh] = new_dist
                        heappush(heap, (new_dist, neigh))

        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)