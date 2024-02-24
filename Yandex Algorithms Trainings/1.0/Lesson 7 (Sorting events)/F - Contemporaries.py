import datetime

# считываем данные
N = int(input().strip())  # N — количество людей
events = []  # массив моментов жизни людей

# добавляем даты в массив событий
for i in range(1, N + 1):
    d1, m1, e1, d2, m2, e2 = map(int, input().split())
    # переводим полученные даты в дни
    start = (datetime.datetime(e1, m1, d1) - datetime.datetime(1, 1, 1)).days
    end = (datetime.datetime(e2, m2, d2) - datetime.datetime(1, 1, 1)).days
    delta_18 = (datetime.datetime(e1 + 18, m1, d1) - datetime.datetime(1, 1, 1)).days
    delta_80 = (datetime.datetime(e1 + 80, m1, d1) - datetime.datetime(1, 1, 1)).days

    # если человек дожил до 18, добавляем в events дату 18 лет, а также минимальное из (end, 80 лет)
    if delta_18 < end:
        events.append((delta_18, 1, i))
        events.append((min(end, delta_80), - 1, i))

# сортируем события
events.sort()

answer = []  # массив ответов
cur_people = set()  # текущее множество современников
updated = False  # флаг обновления множества
# проходим по событиям
for i in range(len(events)):
    # когда человек достиг 18 - добавляем индекс в cur_people и устанавливаем флаг обновления множества True
    if events[i][1] == 1:
        cur_people.add(events[i][2])
        updated = True
    # иначе, если человек вышел из числа современников
    else:
        # если множество было обновлено, то сохраняем его в ответ, убираем флаг updated
        if updated:
            answer.append(list(cur_people))
            updated = False
        # убираем индекс человека из множества
        cur_people.remove(events[i][2])

# ответ
if not answer:
    print(0)
else:
    # группировка множеств современников для печати
    print('\n'.join([' '.join([str(c) for c in group]) for group in answer]))
