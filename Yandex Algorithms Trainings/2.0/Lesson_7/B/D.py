# считываем данные
n, m = map(int, input().split())  # n котят, m отрезков
cats_start = [0] * m  # количество котят к началу каждого отрезка
answer = [0] * m  # количество котят на отрезках
segments = [(x, 0) for x in list(map(int, input().split()))]  # массив событий, котят добавляем с флагом 0

for i in range(m):
    start, end = map(int, input().split())
    segments.append((start, -1, i))  # начало отрезка с флагом -1
    segments.append((end, 1, i))  # конец отрезка с флагом 1

segments.sort()  # сортируем список

all_cats = 0  # текущая префиксная сумма котят
for event in segments:  # проходим по событияем
    if event[1] == 0:  # если котенок - увеличиваем преф сумму
        all_cats += 1
    elif event[1] == -1:  # если начало отрезка - сохраняем в cats_start текущее количество all_cats
        cats_start[event[2]] = all_cats
    else:  # если конец отрезка - сохраняем в ответ разность текущей преф суммы и суммы на начале отрезка
        answer[event[2]] = all_cats - cats_start[event[2]]
# ответ
print(*answer)