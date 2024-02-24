a = int(input().strip())
b = int(input().strip())
n = int(input().strip())
m = int(input().strip())

min_a = a * (n - 1) + n
max_a = a * (n + 1) + n

min_b = b * (m - 1) + m
max_b = b * (m + 1) + m
if min_a <= max_b and min_b <= max_a:
    print(max(min_a, min_b), min(max_a, max_b))
else:
    print(-1)

