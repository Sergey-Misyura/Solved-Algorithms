# считываем данные
n, k = map(int, input().split())  # количество точек и число отрезков
coords = list(map(int, input().split()))  # координаты точек
coords.sort()
# бин поиск по ответу
lf, rg = 0, coords[-1] - coords[0]  # левая, правая границы
while lf < rg:
    mid = (rg + lf) // 2
    count_lines = 0  # количество отрезков, покрывающих точки
    max_right = coords[0] - 1   # самая правая координата текущего отрезка
    # проходим по точкам, считаем количество покрывающих отрезков
    for now_point in coords:
        if now_point > max_right:  # если точка правее текущего отрезка - создаем новый
            count_lines += 1
            max_right = now_point + mid
    # если не более чем необходимо - двигаем rg, иначе lf
    if count_lines <= k:
        rg = mid
    else:
        lf = mid + 1

# ответ
print(lf)
