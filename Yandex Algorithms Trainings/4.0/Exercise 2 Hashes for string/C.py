s = input().strip()

n = len(s)
p = 10 ** 9 + 7
x_ = 257
h = [0] * (n + 1)
x = [0] * (n + 1)
x[0] = 1
s = ' ' + s

for i in range(1, n+1):
    h[i] = (h[i - 1] * x_ + ord(s[i])) % p
    x[i] = (x[i - 1] * x_) % p


def isequal(from1, from2, slen):
    return (h[from1 + slen - 1] + h[from2 - 1] * x[slen]) % p == \
           (h[from2 + slen - 1] + h[from1 - 1] * x[slen]) % p

z = [0] * (n + 1)

for i in range(2, n+1):
    lf = 0
    rg = n + 1 - i

    #binary_search
    while lf <= rg:
        mid = (lf + rg) // 2
        if isequal(1, i, mid):
            lf = mid + 1
        else:
            rg = mid - 1

    z[i] = lf - 1

print(*z[1:])