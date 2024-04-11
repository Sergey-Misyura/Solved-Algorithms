def waterright(now, ynow):
    poly = [(x[now], ynow), (x[now], y[now])]
    for j in range(now + 1, n + 2):
        lastind = j
        if y[j] > ynow:
            break
        poly.append((x[j], y[j]))
    lastx = x[lastind - 1] + (x[lastind] - x[lastind - 1]) * (ynow - y[lastind - 1]) / (y[lastind] - y[lastind - 1])
    poly.append((lastx, ynow))
    poly.append((x[now], ynow))
    square = 0
    for i in range(len(poly) - 1):
        square += poly[i][0] * poly[i + 1][1] - poly[i][1] * poly[i + 1][0]
    square = abs(square) / 2
    water = (x[lastind] - x[now]) * h + sufadd[lastind]
    return water - square

def waterleft(now, ynow):
    poly = [(x[now], ynow), (x[now], y[now])]
    for j in range(now - 1, -1, -1):
        lastind = j
        if y[j] > ynow:
            break
        poly.append((x[j], y[j]))
    lastx = x[lastind + 1] + (x[lastind + 1] - x[lastind]) * (y[lastind + 1] - ynow) / (y[lastind] - y[lastind + 1])
    poly.append((lastx, ynow))
    poly.append((x[now], ynow))
    square = 0
    for i in range(len(poly) - 1):
        square += poly[i][0] * poly[i + 1][1] - poly[i][1] * poly[i + 1][0]
    square = abs(square) / 2
    water = (x[now] - x[lastind]) * h + prefadd[lastind]
    return water - square

def check(m):
    for i in range(1, n + 1):
        if y[i - 1] > y[i] < y[i + 1]:
            square = waterleft(i, y[i] + m) + waterright(i, y[i] + m)
            if square >= 0:
                return True
    return False

n, h = input().split()
n = int(n)
n += 1
h = float(h)
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x = [x[0]] + x + [x[-1]]
y = [100000] + y + [100000]
sufadd = [0] * (n + 2)
for i in range(n, 0, -1):
    sufadd[i] = max(0, waterright(i, y[i]))
prefadd = [0] * (n + 2)
for i in range(1, n + 1):
    prefadd[i] = max(0, waterleft(i, y[i]))
l = 0
r = 10**10
while r - l > 0.000001:
    m = (l + r) / 2
    if check(m):
        l = m
    else:
        r = m
print(l)