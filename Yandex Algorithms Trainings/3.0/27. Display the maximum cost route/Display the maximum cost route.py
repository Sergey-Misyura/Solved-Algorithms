N, M = tuple(map(int, input().split()))
dp = [[-1]*(M+1)]
for i in range(1,N+1):
    dp.append([-1]+list(map(int, input().split())))

dp[0][1] =dp[1][0]= 0
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] += max(dp[i][j-1], dp[i-1][j])
       

i, j, dir = N, M, []
while i!=1 or j!=1:
    if dp[i-1][j]>dp[i][j-1]:
        dir.append('D')
        i-=1
    else:
        dir.append('R')
        j-=1
       
print(dp[N][M])
print(' '.join(dir[::-1]))