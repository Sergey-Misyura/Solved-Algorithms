def check(m):
    r = 0
    pmx = -10**9
    pmn = 10**9
    for i in range(n):
        while r < n and x[r] < x[i] + m:
            r += 1
        mx = pmx
        mn = pmn
        if r != n:
            mx = max(mx, sufmax[r])
            mn = min(mn, sufmin[r])
        if mx - mn < m:
            return True
        pmx = prefmax[i]
        pmn = prefmin[i]
    return False


w, h, n = map(int, input().split())
a = []
for i in range(n):
    a.append(tuple(map(int, input().split())))
a.sort()
x = []
y = []
for now in a:
    x.append(now[0])
    y.append(now[1])
prefmin = [y[0]] * n
prefmax = [y[0]] * n
sufmin = [y[-1]] * n
sufmax = [y[-1]] * n
for i in range(1, n):
    prefmin[i] = min(prefmin[i - 1], y[i])
    prefmax[i] = max(prefmax[i - 1], y[i])
for i in range(n - 2, -1, -1):
    sufmin[i] = min(sufmin[i + 1], y[i])
    sufmax[i] = max(sufmax[i + 1], y[i])
l = 0
r = min(w, h)
while l < r:
    m = (l + r) // 2
    if check(m):
        r = m
    else:
        l = m + 1
print(l)





