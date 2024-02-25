# считываем данные
seq = input().strip()  # последовательность
n = len(seq)  # длина последовательности

# при длине 1 ответ стоимость 0
if n == 1:
    print(0)
else:
    cost = 0  # стоимость замены
    lf, rg = 0, n - 1  # левый, правый указатели
    # пока указатели не сошшлись
    while lf < rg:
        # если буквы не одинаковы - увеличиваем cost на 1
        if seq[lf] != seq[rg]:
            cost += 1
        lf += 1; rg -= 1

    # ответ
    print(cost)