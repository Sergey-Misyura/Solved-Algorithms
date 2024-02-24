s = list(map(int, input().split()))

if len(s) == 2:
    print(*sorted([s[0], s[1]]))
else:
    pos1, pos2 = float('-inf'), float('-inf')
    neg1, neg2 = float('inf'), float('inf')

    for i in range(len(s)):
        if s[i] >= pos1:
            pos1, pos2 = s[i], pos1
        elif s[i] > pos2:
            pos2 = s[i]

        if s[i] <= neg1:
            neg1, neg2 = s[i], neg1
        elif s[i] < neg2:
            neg2 = s[i]

    if pos1*pos2 > neg1*neg2:
        print(*sorted([pos1, pos2]))
    else:
        print(*sorted([neg1, neg2]))


