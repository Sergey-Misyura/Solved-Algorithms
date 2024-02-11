A = int(input().strip())
B = int(input().strip())
C = int(input().strip())
D = int(input().strip())
E = int(input().strip())

brick_min = sorted([A, B, C])
hole_min = sorted([D, E])

ans = True
for i in range(2):
    if ans and hole_min[i] < brick_min[i]:
        ans = False

if ans:
    print('YES')
else:
    print('NO')