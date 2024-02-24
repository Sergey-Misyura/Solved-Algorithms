N = int(input().strip())
s = list(map(int, input().split()))
x = int(input().strip())

if not s:
    print('')
else:
    cur_eq = 0
    cur_diff = abs(s[0] - x)
    for i in range(1, len(s)):
        next_diff = abs(s[i] - x)
        if next_diff < cur_diff:
            cur_eq = i
            cur_diff = next_diff

print(s[cur_eq])


