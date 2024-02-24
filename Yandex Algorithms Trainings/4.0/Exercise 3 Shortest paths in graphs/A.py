N, S, F = map(int, input().split())

matrix = [[-1 for _ in range(N+1)]] + [[] for _ in range(N)]
for i in range(N):
    row = [-1] + list(map(int, input().split()))
    matrix[i+1] = row

distances = [float('inf') for _ in range(N+1)]
visited = [True] + [False for _ in range(N)]

cur_v = S
distances[cur_v] = 0
while not visited[cur_v]:
    for next_v in range(1, N + 1):
        if matrix[cur_v][next_v] != -1:
            distances[next_v] = min(distances[next_v], distances[cur_v] + matrix[cur_v][next_v])
    visited[cur_v] = True

    min_dist = float('inf')
    for i in range(1, N+1):
        if distances[i] < min_dist and not visited[i]:
            cur_v = i
            min_dist = distances[i]

    if min_dist == float('inf'):
        break

if distances[F] != float('inf'):
    print(distances[F])
else:
    print(-1)

