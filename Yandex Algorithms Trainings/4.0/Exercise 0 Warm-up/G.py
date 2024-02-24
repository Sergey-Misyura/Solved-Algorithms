reader = open('input.txt', 'r')

n, m = map(int, reader.readline().split())
field = [[0]*(m+2) for _ in range(n+1)]

for i in range(1, n + 1):
    field[i] = [0] + list(map(int, reader.readline().split()))

reader.close()

max_side = 0
for row in range(1, n+1):
    for col in range(1, m+1):
        if field[row][col] != 0:
            field[row][col] += min(field[row][col-1], field[row-1][col], field[row-1][col-1])
            max_side = max(field[row][col], max_side)

print(max_side)