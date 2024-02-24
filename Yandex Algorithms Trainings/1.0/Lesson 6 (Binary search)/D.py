from math import ceil

# считываем данные
n, a, b, w, h = map(int, input().split())

# используем ПРАВЫЙ бин поиск для первой расстановки
lf, rg = 0, (max(w, h) - min(a, b)) // 2
while lf < rg:
    # считаем центр
    mid = (lf + rg) // 2 + 1
    # считаем строки и столбцы домов
    rows = h // (a+2*mid)
    if rows == 0:
        rg = mid - 1
    else:
        cols = ceil(n/rows)
        if cols > 0 and cols * (b+2*mid) <= w:
            lf = mid
        # если дома не поместились, сдвигаем правый указатель на mid - 1
        else:
            rg = mid - 1

lf_forward = lf

# используем ПРАВЫЙ бин поиск для расстановки, повернув дома на 90
lf, rg = 0, (max(w, h) - min(a, b)) // 2
while lf < rg:
    # считаем центр
    mid = (lf + rg) // 2 + 1
    # считаем строки и столбцы домов
    rows = h // (b+2*mid)
    if rows == 0:
        rg = mid - 1
    else:
        cols = ceil(n/rows)
        if cols > 0 and cols * (a+2*mid) <= w:
            lf = mid
        # если дома не поместились, сдвигаем правый указатель на mid - 1
        else:
            rg = mid - 1
# ответ
print(max(lf, lf_forward))