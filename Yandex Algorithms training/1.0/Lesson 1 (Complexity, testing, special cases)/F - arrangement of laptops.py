a1, a2, b1, b2 = map(int, input().split())
min_a = min(a1, a2)

vars = [(a1+b1, max(a2, b2)),
        (a2+b1, max(a1, b2)),
        (b2+a1, max(b1, a2)),
        (a2+b2, max(a1, b1))]

ans = min(vars, key=lambda x: x[0] * x[1])

print(ans[0], ans[1])