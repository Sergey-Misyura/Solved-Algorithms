from heapq import heappop, heappush

# считываем данные
N, D = map(int, input().split())  # N студентов, D - расстояние разговора
coords = list(map(int, input().split()))  # координаты студентов на оси

# добавляем в массив сортировки событий координату Х студента и X+D - максимальную координату разговора
# X - D не нужно, так как мы добавляем новый номер новому студенты, занятые номера не используем
scanline = []
for i, coord in enumerate(coords):
    scanline.append((coord, -1, i))
    scanline.append((coord + D, 1, i))
# сортировка массива
scanline.sort()

max_var = 0  # максимальный вариант
heap = list(range(1, N + 1))  # heap минимумов, для получение минимально возможного варианта, заполнена номерами по количеству студентов
answer = [0] * N  # массив ответа

# проходим по событиям в массиве событий
for place in scanline:
    coord, flag, idx = place
    # нашли студента - добавляем ему минимальный вариант из heap, обновляем max_var
    if flag == -1:
        var_number = heappop(heap)
        max_var = max(max_var, var_number)
        answer[idx] = var_number
    # достигли дальности разговора студента - возврщаем номер варианта студента в heap
    elif flag == 1:
        var_number = answer[idx]
        heappush(heap, var_number)

# ответ
print(max_var)
print(*answer)



