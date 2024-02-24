# считываем данные
N, M = map(int, input().split())  # число студентов и число преподавателей
places = []  # места за которыми следят преподаватели

# добавляем данные, проверяя концы и начала отрезков
for _ in range(M):
    a, b = map(int, input().split())
    if a <= N:
        b = min(b, N)
        places.append([a, b])

# сортируем места
places.sort()
# массив соединенных отрезков мест
total_places = [places[0]]
# проходим по отрезкам и добавляем в новый массив соединенные отрезки
for i in range(1, M):
    # если отрезки пересекаются - соединим их
    if total_places[-1][1] >= places[i][0]:
        total_places[-1][1] = max(total_places[-1][1], places[i][1])
    # иначе просто добавим в total_places
    else:
        total_places.append(places[i])

answer = N  # ответ
# проходим по массиву total_places и уменьшаем answer на длину отрезка мест
for cur_places in total_places:
    answer -= cur_places[1] - cur_places[0] + 1

# ответ
print(answer)