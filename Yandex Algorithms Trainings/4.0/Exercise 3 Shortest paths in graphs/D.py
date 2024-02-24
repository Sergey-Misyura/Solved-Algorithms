import heapq

reader = open('input.txt', 'r')
N = int(reader.readline().strip())
d, v = map(int, reader.readline().strip().split())
R = int(reader.readline().strip())

schedule = [[] for _ in range(N+1)]
for i in range(R):
    frm_, t_dep, to_, t_arr = map(int, reader.readline().strip().split())
    schedule[frm_].append((to_, t_dep, t_arr))

reader.close()

distances = [float('inf') for _ in range(N+1)]
visited = [True] + [False for _ in range(N)]

dist_heap = [(0, d)]
heapq.heapify(dist_heap)
cur_village = d
distances[d] = 0
while not visited[cur_village]:
    for next_village, time_from, time_to in schedule[cur_village]:
        if distances[cur_village] <= time_from and time_to < distances[next_village]:
            distances[next_village] = time_to
            heapq.heappush(dist_heap, (distances[next_village], next_village))
    visited[cur_village] = True

    l = float('inf')  # current distance from heap
    while not (not visited[cur_village] and l == distances[cur_village]) and dist_heap:
        l, cur_village = heapq.heappop(dist_heap)


if distances[v] != float('inf'):
    print(distances[v])
else:
    print(-1)

