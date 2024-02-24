# счиnsваем данные
a = int(input().strip())  # двоек
b = int(input().strip())  # троек
c = int(input().strip())  # четверок

# предподсчет текущего количества оценок и их суммы
count_score = a+b+c
prod = a*2 + b*3 + c*4

lf, rg = 0, a+b+c  # границы бинпоиска от 0 до суммы числа оценок
# левый бин поиск
while lf < rg:
    # считаем центр
    mid = (lf + rg) // 2
    # если итоговая оценка < 3.5 - сдвигаем lf на mid + 1
    if (mid*5 + prod) < 3.5 * (count_score + mid):
        lf = mid + 1
    # иначе сдвигаем rg на mid
    else:
        rg = mid

# ответ
print(lf)