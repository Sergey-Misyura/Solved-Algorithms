s = list(map(int, input().split()))

if len(s) < 3:
    total = 0
else:
    total = 0
    prev = s[1] > s[0]

    for i in range(1, len(s) - 1):
        next_ = s[i] > s[i+1]
        if prev and next_:
            total += 1

        prev = not next_

print(total)


