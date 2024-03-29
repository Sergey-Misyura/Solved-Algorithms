# считываем данные
n = int(input().strip())
events = []  # массив событий
for i in range(1, n + 1):
    start, end = map(int, input().split())
    events.append((start, i))
    events.append((end, -i))  # окончание цивилизации раньше начала следующей
events.sort()  # сортируем массив

now_civs = set()  # текущие цивилизации
min_intersect = events[-1][0] - events[0][0] + 1  # минимальное пересечение цивилизаций
answer = [0]  # ответ
for event in events:  # проходим по событиям
    if event[1] > 0:  # если событие начало цивилизации - добавляем в множество, сохраняем в prev_start
        now_civs.add(event[1])
        prev_start = event
    else:  # если событие - конец цивилизации
        if event[0] - prev_start[0] < min_intersect:  # если пересечение меньше найденного ранее
            if prev_start[1] != -event[1]:  # если предыдущая цивилизация отлична от текущей - обновляем ответ и min_intersect
                answer = prev_start[1], -event[1]
                min_intersect = event[0] - prev_start[0]
            else:  # иначе, если закончилась только начавшаяся цивилизация
                if len(now_civs) > 1:  # проверяем вложена ли она в другие, если да
                    iter_now_civs = iter(now_civs)  # создание итератора из множества
                    biggest_civ = next(iter_now_civs)  # получение самой дальней цивилизации
                    if biggest_civ == -event[1]:  # если самая дальняя - это текущая, берем следующуу цивилизацию
                        biggest_civ = next(iter_now_civs)
                    min_intersect = event[0] - prev_start[0]  # обновляем длину пересечения (длина текущей цивилизации)
                    answer = biggest_civ, -event[-1]  # обновляем ответ, (самая дальняя и текущая, вложенная в нее)
        now_civs.discard(-event[1])  # убираем закончившуюся цивилизацию из множества
# ответ
print(*sorted(answer))
