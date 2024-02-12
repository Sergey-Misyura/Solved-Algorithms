N = int(input().strip())
s = list(map(int, input().split()))

if len(s) == 1:
     print(0)
else:
    min_seq_len = float('inf')
    ans_seq = []

    for i in range(N // 2, N):
        if min_seq_len != float('inf'):
            break

        lf = max(0, i-(N-i+1))

        if lf != 0:
            if s[i:] == s[i-1:lf:-1]:
                min_seq_len = i - (N - i)
        else:
            if s[i:] == s[i-1::-1]:
                min_seq_len = i - (N - i)

        lf = max(-1, i - (N - i - 1) - 1)
        if lf != -1:
            if s[i+1:] == s[i-1:lf:-1]:
                min_seq_len = min(min_seq_len, i - (N - i - 1))
        else:
            if s[i+1:] == s[i-1::-1]:
                min_seq_len = min(min_seq_len, i - (N - i - 1))


    if min_seq_len == float('inf'):
        print(N - 1)
        print(*s[N-2::-1])
    else:
        print(min_seq_len)
        if min_seq_len != 0:
            print(*s[min_seq_len-1::-1])

