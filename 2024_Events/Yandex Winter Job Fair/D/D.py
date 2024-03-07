n, x = map(int, input().split())
a = list(map(int, input().split()))

sum_a = sum(a)
c = [0 for _ in range(n)]
rems = [0 for _ in range(n)]

for i in range(n):
    quot, rem = divmod(a[i]*x, sum_a)
    c[i] = quot
    rems[i] = (rem, i)
rems.sort()

lf = 0
rg = n - 1
for i in range(x - sum(c)):

    if abs(sum_a - rems[rg][0] + rems[lf][0]) <= abs(sum_a - rems[lf][0] + rems[rg][0]):
        c[rems[rg][1]] += 1
        rg -= 1
    else:
        c[rems[lf][1]] += 1
        lf += 1


print(*c)





