def issquare(i, j, k):
    return sums[i][j] - sums[i - k][j] - sums[i][j - k] + sums[i - k][j - k] == k ** 2


def check(k):
    for i in range(1, n - 2 * k + 1):
        for j in range(1, m - 2 * k + 1):
            if issquare(i, j + k, k) and \
                    issquare(i + k, j, k) and \
                    issquare(i + k, j + k, k) and \
                    issquare(i + k, j + k * 2, k) and \
                    issquare(i + k * 2, j + k, k):
                return True
    return False



n, m = map(int, input().split())
sums = [[0] * (m + 1)]
for i in range(n):
    sums.append([0] * (m + 1))
    s = '.' + input()
    for j in range(1, m + 1):
        sums[i][j] = sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1]
        if s[j] == '#':
            sums[i][j] += 1
l = 1
r = n
while l < r:
    mid = (l + r + 1) // 2
    if check(mid):
        l = mid
    else:
        r = mid - 1
print(l)
