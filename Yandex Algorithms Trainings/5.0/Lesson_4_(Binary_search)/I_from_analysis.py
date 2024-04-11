def pointincircle(x0, y0, r0, xp, yp):
    return (xp - x0) ** 2 + (yp - y0)**2 - r0**2 < 0.000001

def checkrect(xll, yll, xru, yru, time):
    if not pointincircle(0, 0, d, xll, yll) and \
        not pointincircle(0, 0, d, xll, yru) and \
        not pointincircle(0, 0, d, xru, yll) and \
        not pointincircle(0, 0, d, xru, yru):
        return (False, (0, 0))
    if xru - xll < 0.000001:
        return (True, ((xll + xru) / 2, (yll + yru) / 2))
    for i in range(n):
        if pointincircle(x[i], y[i], v[i] * time, xll, yll) and \
            pointincircle(x[i], y[i], v[i] * time, xll, yru) and \
            pointincircle(x[i], y[i], v[i] * time, xru, yll) and \
            pointincircle(x[i], y[i], v[i] * time, xru, yru):
            return (False, (0, 0))
    xs = [xll, (xll + xru) / 2, xru]
    ys = [yll, (yll + yru) / 2, yru]
    for i in range(2):
        for j in range(2):
            quarter = checkrect(xs[i], ys[j], xs[i + 1], ys[j + 1], time)
            if quarter[0]:
                return quarter
    return (False, (0, 0))

def check(time):
    return checkrect(-d, 0, d, d, time)

d, n = map(int, input().split())
x = []
y = []
v = []
for i in range(n):
    a, b, c = map(int, input().split())
    x.append(a)
    y.append(b)
    v.append(c)
l = 0
r = 4 * d
while r - l > 0.000001:
    m = (l + r) / 2
    if check(m)[0]:
        l = m
    else:
        r = m
now = check(l)
print(l)
print(*now[1])

