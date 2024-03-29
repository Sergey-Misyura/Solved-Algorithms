# считываем данные, (a * x + b) / (c * x + d) = 0
a = int(input().strip())
b = int(input().strip())
c = int(input().strip())
d = int(input().strip())

# ветвление в соответствии с условиями задачи
if a == 0 and b == 0:
    print('INF')
elif b != 0:
    if a == 0:
        print('NO')
    else:
        x = - b / a
        # проверка х и проверка знаменателя на 0
        if x == int(x) and c * int(x) + d != 0:
            print(int(x))
        else:
            print('NO')
