# считываем данные
N = int(input().strip())  # количество учеников
houses = list(map(int, input().split()))  # координаты домов учеников
norm_houses = [house - houses[0] for house in houses]  # нормированные координаты домов от 0

cur_houses_left = 0  # текущее число домов слева по оси
cur_houses_right = N - 1  # текущее число домов справа по оси
min_dist = sum(norm_houses)  # минимальная общая дистанция пути учеников
best_idx = 0  # индекс лучшего расположения школы
cur_dist = min_dist  # текущая общая дистанция пути учеников
# проходим по массиву домов
for i in range(1, N):
    # считаем изменение дистанции
    diff = norm_houses[i] - norm_houses[i - 1]
    # увеличиваем счетчик домов слева
    cur_houses_left += 1
    # пересчитываем текущую общую дистанцию
    cur_dist = cur_dist + (cur_houses_left - cur_houses_right) * diff
    # уменьшаем счетчик домов справа
    cur_houses_right -= 1
    # когда нашли дистанцию меньше лушей меньшей - сохраняем ее и индекс
    if cur_dist < min_dist:
        min_dist = cur_dist
        best_idx = i

# ответ
print(houses[best_idx])



