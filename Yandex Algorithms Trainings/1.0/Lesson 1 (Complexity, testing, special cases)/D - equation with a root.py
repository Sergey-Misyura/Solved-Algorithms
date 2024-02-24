a = int(input().strip())
b = int(input().strip())
c = int(input().strip())


if c < 0:
    print('NO SOLUTION')
elif a == 0:
    if c**2 == b:
        print('MANY SOLUTIONS')
    else:
        print('NO SOLUTION')
else:
    ans = (c**2 - b) / a
    if ans - int(ans):
        print('NO SOLUTION')
    else:
        print(int(ans))