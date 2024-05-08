n = int(input())
a = list(map(int, input().split()))
a.sort()

len_a = len(a)
count = 0
lf, rg = 0, len(a) - 1
while lf < rg:
    mid = (lf + rg) // 2
    cur = int(a[mid]**0.5)
    if cur <= len_a - mid:
        lf = mid + 1
        count = max(count, cur)
    else:
        rg = mid
if count == 0 and a[0] > 0:
    print(len(a))
else:
    print(count)