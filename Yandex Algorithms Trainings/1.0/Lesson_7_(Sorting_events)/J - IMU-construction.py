# считываем данные
N, W, L = map(int, input().split())  # N — количество возможных блоков, W и L - размеры комплекса
total_area = W * L  # общая площадь комплекса
events = []  # массив событий
# добавляем блоки в events, сведя задачу к двумерной: (z, площадь x*y)
for i in range(1, N + 1):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    # считаем площадь по осям x и y
    area = abs(x2 - x1) * abs(y2 - y1)
    # добавляем в события площадь с z координатами, начало с 1, конец с -1, для исключения перекрытий нулевой толщины
    events.append((z1, 1, area, i))
    events.append((z2, -1, area, i))
# сортировка events
events.sort()
min_used = N + 1  # минимальное число используемых блоков
now_used = 0  # текущее число используемых блоков
now_area = 0  # текущая занятая площадь
# проходим по массиву events
for event in events:
    # если блок начался, увеличиваем счетчик now_used, увеличиваем now_area
    if event[1] == 1:
        now_used += 1
        now_area += event[2]
        # если покрыли площадь и число блоков now_used меньше минимального min_used, обновляем результат
        if now_area == total_area and now_used < min_used:
            min_used = now_used
    # иначе, если блок кончился, уменьшаем счетчик, уменьшаем площадь
    else:
        now_used -= 1
        now_area -= event[2]
# если не нашли ответ - выводим NО
if min_used == N + 1:
    print('NO')
# иначе, выводим YES, число блоков, повторным проходом находим множество использованных для покрытия блоков
else:
    print('YES')
    print(min_used)
    used_blocks = set()  # множество используемых блоков
    # проходим по блокам в events
    for event in events:
        # нашли начало блока - добавляем его в множество, увеличиваем now_used и now_area
        if event[1] == 1:
            now_used += 1
            used_blocks.add(event[3])
            now_area += event[2]
            # нашли все блоки и покрыли площадь - выводим их номера, break
            if now_area == total_area and now_used == min_used:
                print(*used_blocks)
                break
        # иначе, нашли конец блока - убираем его из множества used_blocks, уменьшаем now_used, now_area
        else:
            now_used -= 1
            used_blocks.remove(event[3])
            now_area -= event[2]
