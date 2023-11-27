k = int(input())

for _ in range(k):
    n, a, b = map(int, input().split())
    min_count_groups, rem = divmod(n, a)
    if min_count_groups == 0:
        print('NO')
    else:
        if (b - a)*min_count_groups >= rem:
            print('YES')
        else:
            print('NO')