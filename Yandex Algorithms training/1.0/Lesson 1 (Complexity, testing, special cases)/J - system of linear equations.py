a = float(input().strip())
b = float(input().strip())
c = float(input().strip())
d = float(input().strip())
e = float(input().strip())
f = float(input().strip())


if (a * d - b * c) != 0:
    if d != 0:
        x = (e - b * f / d ) / (a - b * c / d)
        y = (f - c * x) / d
        print(2, x, y)
    else:
        x = (f - d * e / b) / (c - d * a / b)
        y = (e - a * x) / b
        print(2, x, y)
else:
    if a == 0 and c == 0:
        if b == 0 and d == 0:
            if e == 0 and f == 0:
                print(5)
            else:
                print(0)
        elif e * d != f * b:
            print(0)
        else:
            if b != 0:
                print(4, e/b)
            else:
                print(4, f/d)

    elif b == 0 and d == 0:
        if e * c != f * a:
            print(0)
        else:
            if a != 0:
                print(3, e / a)
            else:
                print(3, f / c)
    elif a != 0:
        coef = c / a
        if d == b * coef and f == e * coef:
            print(1, -a / b, e / b)
        else:
            print(0)
    else:
        coef = a / c
        if b == coef * d and e == coef * f:
            print(1, -c / d, f / d)
        else:
            print(0)
