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

max_pref = -1
cur_len = n - 1
while max_pref == -1 and cur_len > 0:
    if isequal(1, n + 1 - cur_len,cur_len):
        max_pref = cur_len
    cur_len -= 1

if max_pref != -1:
    print(n - max_pref)
else:
    print(n)
