# считываем данные
x, y, z = map(int, input().split())  # запись даты

# если x, y меньше или равны 12
if x <= 12 and y <= 12:
    # если числа одинаковы, то можно однозначно установить дату - выводим 1
    if x == y:
        print(1)
    # иначе выводим 0
    else:
        print(0)
# в противном случае выводим 1
else:
    print(1)

