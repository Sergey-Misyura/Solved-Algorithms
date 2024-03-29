k = int(input())
v = [(0, 0)] * (k + 4)
for i in range(k):
    a, n = map(int, input().split())
    v[i + 2] = [a, n]
for i in [0, 1, len(v) - 1, len(v) - 2]:
    v[i] = [0, 0]
p = [2, len(v) - 3]
p1 = p[0]
p2 = p[1]
while True:
    if p1 == p2 and v[p1][1] == 1:
        print(1)
        print(v[p1][0])
        break
    if p1 == p2 and v[p1][1] == 2 or p1 == p2 - 1 and v[p1][1] == 1 and v[p2][1] == 1:
        print(2)
        print(v[p1][0], v[p2][0])
        break
    for dir in range(len(p)):
        shift = 1 if dir == 0 else -1
        cur_p = p[dir]
        cnt = 0
        for i in [cur_p, cur_p + shift]:
            if v[i][1] == 1:
                cnt += 1
            else:
                break
        if cnt == 0:
            val = v[cur_p][0]
            if v[cur_p][1] > 2:
                v[cur_p][1] -= 2
                v[cur_p - shift] = [val, 1]
                v[cur_p - 2 * shift] = [val, 1]
                cur_p -= 2 * shift
                p[dir] = cur_p
                if dir == 0:
                    p1 = p[dir]
                else:
                    p2 = p[dir]
            elif v[cur_p][1] == 2:
                v[cur_p][1] -= 1
                v[cur_p - shift] = [val, 1]
                cur_p -= shift
                p[dir] = cur_p
                if dir == 0:
                    p1 = p[dir]
                else:
                    p2 = p[dir]
        elif cnt == 1:
            v[cur_p - shift] = v[cur_p]
            val = v[cur_p + shift][0]
            v[cur_p + shift][1] -= 1
            v[cur_p] = [val, 1]
            cur_p -= shift
            p[dir] = cur_p
            if dir == 0:
                p1 = p[dir]
            else:
                p2 = p[dir]

    tmp = min(v[p1][0], v[p2][0])
    v[p1][0] -= tmp
    v[p1 + 1][0] += tmp
    v[p2][0] -= tmp
    v[p2 - 1][0] += tmp

    if v[p1][0] == 0:
        p1 += 1
        p[0] = p1
    if v[p2][0] == 0:
        p2 -= 1
        p[1] = p2