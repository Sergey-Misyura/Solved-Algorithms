from math import ceil

n, t, s = map(int, input().split())
v = list(map(int, input().split()))
first = v[0] * t

total = 0
for i in range(n):
    second = v[i] * t
    total += max(0, ceil((first - second) / s) - 1)

print(total)