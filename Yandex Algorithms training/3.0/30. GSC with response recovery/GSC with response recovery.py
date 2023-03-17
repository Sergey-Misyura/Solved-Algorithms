N = int(input())
seq_1 = [0] + list(map(int, input().split()))
M = int(input())
seq_2 = [0] + list(map(int, input().split()))

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if seq_1[i]==seq_2[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
           
i, j, seq, max_len = N, M, [], dp[N][M]
while len(seq)!=max_len:
    if dp[i][j]!=dp[i-1][j] and dp[i][j]!=dp[i][j-1]:
        seq.append(seq_1[i])
        i -=1
        j -=1
    elif dp[i][j] == dp[i-1][j]:
        i-=1
    else:
        j-=1
   
print(' '.join(str(x) for x in seq[::-1]))