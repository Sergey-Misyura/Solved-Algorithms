from math import pi

# считываем данные
n = int(input().strip())  # количество прямоугольников
events = []  # массив событий
r1, r2, phi1, phi2 = map(float, input().split())  # радиусы окружностей, образующих кольцо; углы, образованные первым и вторым лучами с осью абсцисс, заданные в радианах
rmin = r1  # меньший радиус - максимальный радиус среди внутренних окружностей
rmax = r2  # больший радиус - минимальный радиус среди внешних окружностей
events.append((phi1, -1))
events.append((phi2, 1))
for i in range(2, n + 1):  # добавляем концы полярных прямоугольников в events
    r1, r2, phi1, phi2 = map(float, input().split())
    rmin = max(rmin, r1)
    rmax = min(rmax, r2)
    events.append((phi1, -i))
    events.append((phi2, i))
events.sort()  # сортируем массив событий

# первый проход, подсчитываем число начавшихся на окружности полярных прямоуголников до первого в events
cur_rect = set()  # текущие начавшиеся прямоуголтники
count_segms = 0  # количество начавшихся но не закончившихся прямоугольников
for event in events:  # проходим по events
    if event[1] < 0:  # если прямоугольник начался
        count_segms += 1  # увеличиваем счетчик count_segms
        cur_rect.add(-event[1])  # добавляем прямоугольник в cur_rect
    elif event[1] in cur_rect:  # если прямоугольник закончился - уменьшаем count_segms
        count_segms -= 1

answer = 0  # ответ - площадь пересечения
# второй проход, начинается с уже имеющимися прямоугольниками в count_segms
for i in range(len(events)):  # проходим по event
    event = events[i]
    if event[1] < 0:  # изменяем счетчик count_segms
        count_segms += 1
    else:
        count_segms -= 1
    if count_segms == n:  # когда число начавшихся прямоугольников равно n (если такого случая не будет ответ - 0)
        if i < len(events) - 1:  # если существует следующее событие, оно закроет прямоугольник - считаем площадь пересечения с текущего события до следующего
            answer += (events[i + 1][0] - events[i][0]) * (rmax ** 2 - rmin ** 2) / 2  # сумма для подсчета по "частям" при разбивке по первому событию в events
        else:  # иначе если на последнем событии все прямоугольники уже начались, но не закончился ни один
            # в качестве следующего события используем первое событие в events
            answer += (events[0][0] - events[len(events) - 1][0] + 2 * pi) * (rmax ** 2 - rmin ** 2) / 2

# ответ
print(answer)