N = int(input())
coords = list(map(int, input().split()))

coords.sort()
dp = [0] * (N+1)
dp[0] = dp[1] = 0
dp[2] = coords[1] - coords[0]

if N >= 3:
    dp[3] = dp[2] + coords[2] - coords[1]

if N >=4:
    for i in range(4, N+1):
        dp[i] = min(dp[i-1], dp[i-2]) + (coords[i-1] - coords[i-2])


print(dp[N])