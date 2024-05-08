from collections import defaultdict
import sys

sys.setrecursionlimit(15000)
N = int(input().strip())
if N == 0:
    print(0, 0)
else:
    graph = [[] for _ in range(N)]
    for i in range(N):
        graph[i] = list(map(int, input().split()))
    if N == 1:
        print(1, 1)
    else:
        def path_search(i, j, prev, visited):
            if i < 0 or j < 0 or i == N or j == N:
                return 0, 0  # path_len, count
            if graph[i][j] > prev:
                return 0, 0
            visited.add((i, j))
            paths = []
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                cur_i, cur_j = i + di, j + dj
                if (cur_i, cur_j) not in visited:
                    p, c = path_search(cur_i, cur_j, graph[i][j], visited.copy())
                    paths.append((p + 1, c))
            if not paths:
                return 1, 0
            path_len = max(paths)[0]
            count = 0
            for path in paths:
                if path[0] == path_len:
                    count += path[1]
            return path_len, count or 1


        answer = defaultdict(int)

        for j in range(0, N):
            path_len, count = path_search(0, j, 10001, set())
            answer[path_len] += count
            path_len, count = path_search(N - 1, j, 10001, set())
            answer[path_len] += count
        for i in range(1, N - 1):
            path_len, count = path_search(i, 0, 10001, set())
            answer[path_len] += count
            path_len, count = path_search(i, N - 1, 10001, set())
            answer[path_len] += count

        max_len_path = max(answer)
        print(max_len_path, answer[max_len_path])