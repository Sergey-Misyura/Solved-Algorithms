# считываем данные
n, m = map(int, input().split())  # n отрезков и m точек
scanline = []  # общий массив концов отрезков и точек

# добавляем отрезки в массив scanline для дальнейшей сортировки - начала отрезков с флагом -1, концы с 1
for _ in range(n):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    scanline.append((a, -1))
    scanline.append((b, 1))

dots = list(map(int, input().split()))  # точки
# добавляем точки в scanline, с флагом 0
for i in range(m):
    scanline.append((dots[i], 0, i))

# сортируем массив
scanline.sort()
answer = [0] * m  # массив ответа
cur_count = 0  # количество отрезков в текущей точке
# проходим по массиву scanline
for dot in scanline:
    # так как для сортировки использовались флаги (-1, 0, 1), то для подсчета cur_count вычитаем флаг
    cur_count -= dot[1]
    # если нашли точку, сохраняем в ответ под нужным индексом cur_count отрезков
    if dot[1] == 0:
        answer[dot[2]] = cur_count

# ответ
print(*answer)

