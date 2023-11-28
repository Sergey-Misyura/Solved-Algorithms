a, b, c, d = map(int, input().split())
num = a*d + c*b
denom = b*d


if num > denom:
    nod = num
else:
    nod = denom
while nod != 1:
    if num % nod == 0 and denom % nod == 0:
        print(num // nod, denom // nod, sep=' ')
        break
    else:
        nod -= 1
if nod == 1:
    print(num, denom, sep=' ')