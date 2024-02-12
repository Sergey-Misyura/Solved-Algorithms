s = list(map(int, input().split()))

if len(s) == 3:
    print(s[0], s[1], s[2])
else:
    pos1, pos2, pos3 = float('-inf'), float('-inf'), float('-inf')
    neg1, neg2 = float('inf'), float('inf')

    for i in range(len(s)):
        if s[i] >= pos1:
            pos1, pos2, pos3 = s[i], pos1, pos2
        elif s[i] >= pos2:
            pos2, pos3 = s[i], pos2
        elif s[i] > pos3:
            pos3 = s[i]

        if s[i] <= neg1:
            neg1, neg2 = s[i], neg1
        elif s[i] < neg2:
            neg2 = s[i]

    if pos1*pos2*pos3 > neg1*neg2*pos1:
        print(pos1, pos2, pos3)
    else:
        print(neg1, neg2, pos1)


