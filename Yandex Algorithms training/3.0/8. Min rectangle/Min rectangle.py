k = int(input())
coords = [list(map(int, input().split())) for _ in range(k)]
min_X, max_X = min(coords, key=lambda x: x[0])[0], max(coords, key=lambda x: x[0])[0]
min_Y, max_Y = min(coords, key=lambda y: y[1])[1], max(coords, key=lambda y: y[1])[1]
print(min_X, min_Y, max_X, max_Y)