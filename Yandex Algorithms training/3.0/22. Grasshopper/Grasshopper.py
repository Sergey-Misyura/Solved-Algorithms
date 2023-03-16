N, k = tuple(map(int,input().split()))


dp = [0] * (N+1)
dp[0] = 0
dp[1] = 1
if N >=2:
    dp[2] = 1
if N >=3:
    for i in range (3, N+1):
        dp[i] = sum(dp[max(2,i-k):i])
        dp[i]+=1 if i-1<=k else 0

   
print(dp[N])