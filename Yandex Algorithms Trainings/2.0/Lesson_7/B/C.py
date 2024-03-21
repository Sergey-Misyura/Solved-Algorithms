# считываем данные
M = int(input().strip())  # правый край отрезка
segments = []  # массив отрезков
start, end = map(int, input().split())
while start != 0 or end != 0:
    if end > 0 and start < M:  # если отрезок пересекается с [0, M] добавляем в массив
        segments.append((start, end))
    start, end = map(int, input().split())
# сортируем отрезки
segments.sort()
answer = []  # массив ответа
cur_rg = 0  # текущее дальность покрытия вправо, сохраненными в ответе отрезками
cur_best_seg = 0, 0  # текущий лучший отрезок
best_seg_rg = 0  # следущее дальность покрытия вправо следующего кандидата
for segment in segments:  # проходим по отрезкам segments
    if segment[0] > cur_rg:  # если следующий отрезок дальше текущей дальности покрытия
        answer.append(cur_best_seg)  # добавляем текущий лучший отрезок к ответу
        cur_rg = best_seg_rg  # обновляем текущую дальность покрытия
        if cur_rg >= M:  # если покрыли M - выходим
            break
    # если начало текущего отрезка меньше дальности покрытия cur_rg а конец дальше чем best_seg_rg
    if segment[0] <= cur_rg and segment[1] > best_seg_rg:
        best_seg_rg = segment[1]  # обновляем дальность покрытия следующего кандидата
        cur_best_seg = segment  # обновляем следующего кандидата
# проверяем последний оставшийся в cur_rg отрезок
if cur_rg < M:
    cur_rg = best_seg_rg
    answer.append(cur_best_seg)

# ответ
if cur_rg < M:  # если не покрыли [0, M] - No solution
    print('No solution')
else:  # иначе выводим длину и отрезки
    print(len(answer))
    print(*[str(a) + ' ' + str(b) for a, b in answer], sep='\n')