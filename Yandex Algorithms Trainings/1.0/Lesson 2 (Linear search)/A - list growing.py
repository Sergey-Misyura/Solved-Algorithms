s = list(map(float, input().split()))

monotonic = True
if len(s) >= 2:
    for i in range(1, len(s)):
        if s[i] <= s[i - 1]:
            monotonic = False
            break

if monotonic:
    print('YES')
else:
    print('NO')