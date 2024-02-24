from collections import defaultdict
import heapq

reader = open('input06.txt', 'r')
N, K = map(int, reader.readline().strip().split())

graph = [[] for _ in range(N+1)]
for i in range(K):
    a, b, l = map(int, reader.readline().strip().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

S, F = map(int, reader.readline().strip().split())
reader.close()

distances = [float('inf') for _ in range(N+1)]
visited = [True] + [False for _ in range(N)]

dist_heap = [(0, S)]
heapq.heapify(dist_heap)
cur_v = S
distances[cur_v] = 0
while not visited[cur_v]:

    for next_v, l in graph[cur_v]:
        if distances[cur_v] + l < distances[next_v]:
            distances[next_v] = distances[cur_v] + l
            heapq.heappush(dist_heap, (distances[next_v], next_v))
    visited[cur_v] = True

    l = float('inf')
    while not (not visited[cur_v] and l == distances[cur_v]) and dist_heap:
        l, cur_v = heapq.heappop(dist_heap)

if distances[F] != float('inf'):
    print(distances[F])
else:
    print(-1)

