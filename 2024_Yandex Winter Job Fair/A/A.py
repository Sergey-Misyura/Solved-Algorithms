n = 8
grid = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
for _ in range(n):
    grid.append(['*'] + list(input()) + ['*'])

grid.append(['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'])

total = 0
for row in range(1, n+1):
    for col in range(1, n+1):
        if grid[row][col] == '.':
            if grid[row][col - 1] == '.' and grid[row][col + 1] == '.':
                if grid[row - 1][col] == '.':
                    total += 1
                if grid[row + 1][col] == '.':
                    total += 1
            if grid[row - 1][col] == '.' and grid[row + 1][col] == '.':
                if grid[row][col - 1] == '.':
                    total += 1
                if grid[row][col + 1] == '.':
                    total += 1

print(total)



