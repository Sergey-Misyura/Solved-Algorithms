"""
1971. Find if Path Exists in Graph
(Easy complexity)

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination false.
"""


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)  # граф
        dq = deque([source])  # очередь вершин
        visited = {source}  # посещенные вершины
        for v1, v2 in edges:  # обновляем граф
            graph[v1].append(v2)
            graph[v2].append(v1)
        while dq:  # пока есть в очереде вершины
            cur_v = dq.popleft()  # достаем вершину
            if cur_v == destination:  # проверяем вершину на целевую
                return True
            for next_v in graph[cur_v]:  # проходим по соседям
                if next_v not in visited:  # если сосед еще не посещен
                    visited.add(next_v)
                    dq.append(next_v)
        # ответ
        return False
