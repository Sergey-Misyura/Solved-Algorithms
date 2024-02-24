N = int(input())
A, B, C = [0] * (N+1), [0] * (N+1), [0] * (N+1)
for n in range (1, N+1):
    A[n], B[n], C[n] = tuple(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = A[1]
if N >= 2:
    dp[2] = min (A[1]+A[2], B[1])
if N >= 3:
    dp[3] = min (A[1]+A[2]+A[3], A[1]+B[2], B[1]+A[3], C[1])
   
if N >= 4:    
    for i in range(4, N+1):
        dp[i] = min(dp[i-1]+A[i], dp[i-2]+B[i-1], dp[i-3]+C[i-2])
 
print(dp[N])