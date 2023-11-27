from math import pi
from math import atan2

xa, ya, xb, yb = map(int, input().split())

len_a = (xa ** 2 + ya ** 2) ** 0.5
len_b = (xb ** 2 + yb ** 2) ** 0.5
if len_a == 0:
    print(f'{len_b:.12f}')
elif len_b == 0:
    print(f'{len_a:.12f}')
else:
    scalar = xa * xb + ya * yb
    if atan2(ya, xa) > atan2(yb, xb):
        alpha = atan2(ya, xa) - atan2(yb, xb)
    else:
        alpha = atan2(yb, xb) - atan2(ya, xa)

    if alpha == 0:
        max_r = max(len_a, len_b)
        min_r = min(len_a, len_b)
        print(f'{max_r - min_r:.12f}')
    elif alpha == pi:
        print(f'{len_a + len_b:.12f}')
    else:
        min_r = min(len_a, len_b)
        arc = min_r * alpha
        dist = arc + max(len_a, len_b) - min_r
        print(f'{min(dist, len_a + len_b):.12f}')