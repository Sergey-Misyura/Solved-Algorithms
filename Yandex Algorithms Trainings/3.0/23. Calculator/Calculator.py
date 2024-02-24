N = int(input())

dp, prev = [0] * (N+1), [0] * (N+1)
dp[0] = dp[1] = 0
prev[0] = prev[1] = 0
if N >=2:
    dp[2], prev[2] = 1, 1
if N >=3:
    dp[3], prev[3] = 1, 1
if N >= 4:
    for i in range(4, N+1):
        if i % 3 == 0 and i % 2 == 0:
            idx = min((dp[i-1], i-1), (dp[i//2], i//2), (dp[i//3], i//3), key = lambda x: x[0])

        elif i % 3 == 0:
            idx = min((dp[i//3], i//3), (dp[i-1], i-1), key = lambda x: x[0])
        elif i % 2 == 0:
            idx = min((dp[i-1], i-1), (dp[i//2], i//2), key = lambda x: x[0])
        else:
            idx = (dp[i-1], i-1)
       
        dp[i], prev[i] = dp[idx[1]]+1, idx[1]

num_list=[]
curr = N
while curr!=0:
    num_list.append(curr)
    curr=prev[curr]

print(dp[N])
print(' '.join([str(x) for x in num_list[::-1]]))