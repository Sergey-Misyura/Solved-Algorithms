N, M = tuple(map(int, input().split()))

dp = [[0]*(M+1) for _ in range(N+1)]
dp[1][1] = 1

for i in range(2, N+1):
    for j in range(2, M+1):
        dp[i][j] = dp[i-1][j-2] + dp[i-2][j-1]
       
print(dp[N][M])