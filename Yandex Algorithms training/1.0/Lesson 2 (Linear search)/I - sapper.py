N, M, K = map(int, input().split())
sapper_grid = [[0]*M for _ in range(N)]


for _ in range(K):
    x, y = map(int, input().split())
    sapper_grid[x - 1][y - 1] = '*'

shifts = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
for i in range(N):
    for j in range(M):
        if sapper_grid[i][j] == '*':
            for dx, dy in shifts:
                if 0 <= i+dx <= N - 1 and 0 <= j+dy <= M - 1:
                    if sapper_grid[i+dx][j+dy] != '*':
                        sapper_grid[i+dx][j+dy] += 1


for line in sapper_grid:
    print(*line)