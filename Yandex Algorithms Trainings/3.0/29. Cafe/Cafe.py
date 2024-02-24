N = int(input())

dinners_cost = [0]

for _ in range(N):
    dinners_cost.append(int(input()))

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dp[0][i] = float('inf')

dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(N + 1):
        if dinners_cost[i] <= 100:
            if j < N:
                dp[i][j] = min(dp[i - 1][j] + dinners_cost[i], dp[i - 1][j + 1])
            else:
                dp[i][j] = dp[i - 1][j] + dinners_cost[i]
        else:
            if j > 0 and j < N:
                dp[i][j] =  min(dp[i - 1][j + 1], dp[i - 1][j - 1] + dinners_cost[i])
            elif j == 0 and j != N:
                dp[i][j] = dp[i - 1][j + 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dinners_cost[i]
               
min_tot_cost = min(dp[-1])


print(min_tot_cost)
cur_idx = list(reversed(dp[-1])).index(min_tot_cost)
print(abs(cur_idx - len(dp[-1]) + 1), end=' ')

used_count, num_days = 0, []
while i > 1:
    j = dp[i].index(min_tot_cost)
    if j == 0:
        if dp[i - 1][j] + dinners_cost[i] == dp[i][j]:
            min_tot_cost -= dinners_cost[i]
        else:
            if dinners_cost[i] != 0:
                used_count += 1
                num_days.append(i)
    elif j == N:
        min_tot_cost -= dinners_cost[i]
    else:
        if dp[i - 1][j] + dinners_cost[i] == dp[i][j] or dp[i - 1][j - 1] + dinners_cost[i] == dp[i][j]:
            min_tot_cost -= dinners_cost[i]
        else:
            if dinners_cost[i] != 0:
                used_count += 1
                num_days.append(i)
    i -= 1

print(used_count)
for i in range(used_count - 1, -1, -1):
    print(num_days[i])