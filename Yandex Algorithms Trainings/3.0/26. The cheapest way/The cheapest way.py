N, M = tuple(map(int, input().split()))
dp = [[10**6]*(M+1)]
for i in range(1,N+1):
    dp.append([10**6]+list(map(int, input().split())))

dp[0][1] =dp[1][0]= 0
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] += min(dp[i][j-1], dp[i-1][j])
       
       
print(dp[N][M])