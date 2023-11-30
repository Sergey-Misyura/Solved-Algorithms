from collections import defaultdict

reader = open('input.txt', 'r')
N = int(reader.readline().strip())

cities = [(float('inf'), float('inf'))] * (N + 1)
for i in range(1, N + 1):
    T, V = map(int, reader.readline().strip().split())
    cities[i] = (T, V)

roads = defaultdict(list)

for _ in range(N - 1):
    A, B, S = map(int, reader.readline().strip().split())
    roads[A].append((B, S))
    roads[B].append((A, S))

reader.close()

ts_matr = [[float('inf') for _ in range(N + 1)] for _ in range(N + 1)]  # time speed matrix


def dfs(start_city):
    ts_matr[start_city][start_city] = cities[start_city][0]
    speed = cities[start_city][1]
    queue = [start_city]
    visited = set()
    while queue:
        cur_city = queue.pop(0)
        visited.add(cur_city)
        for next_city, distance in roads[cur_city]:
            if next_city not in visited:
                prev_time = ts_matr[start_city][cur_city]
                ts_matr[start_city][next_city] = (prev_time + distance / speed)

                queue.append(next_city)

# dfs for every city
for city in range(1, N+1):
    dfs(city)
trans_ts_matr = list(map(list, zip(*ts_matr)))


distances = [float('inf') for _ in range(N+1)]
visited = [True] + [False for _ in range(N)]
prev = [-1 for _ in range(N+1)]

# Dijkstra from V 1
cur_v = 1
distances[cur_v] = 0
while not visited[cur_v]:
    for next_v in range(1, N + 1):
        if trans_ts_matr[cur_v][next_v] != float('inf'):
            if distances[cur_v] + trans_ts_matr[cur_v][next_v] < distances[next_v]:
                distances[next_v] = distances[cur_v] + trans_ts_matr[cur_v][next_v]
                prev[next_v] = cur_v
    visited[cur_v] = True

    min_dist = float('inf')
    for i in range(1, N+1):
        if distances[i] < min_dist and not visited[i]:
            cur_v = i
            min_dist = distances[i]

    if min_dist == float('inf'):
        break

# output max min time
max_min_time = max(distances[1:])
idx_max_min = distances.index(max_min_time)
print(max_min_time)

# output road
if distances[idx_max_min] != float('inf'):
    road = [idx_max_min]
    cur_v = idx_max_min
    while prev[cur_v] != -1:
        road.append(prev[cur_v])
        cur_v = prev[cur_v]
    print(*road)
else:
    print(-1)
