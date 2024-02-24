N, K, M = map(int, input().split())

total_count = 0
total_rem = N
workpieces = 1
details, rem_2_stage = divmod(K, M)

if M == 0 or M > K or K > N:
    print(total_count)
else:
    while workpieces > 0:
        workpieces, rem = divmod(total_rem, K)
        total_count += details * workpieces
        total_rem = rem + rem_2_stage * workpieces

    print(total_count)
