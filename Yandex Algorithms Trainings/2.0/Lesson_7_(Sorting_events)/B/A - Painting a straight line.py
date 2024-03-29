# считываем данные
N = int(input().strip())  # количество отрезков
segments = [0] * N  # массив отрезков
for i in range(N):
    start, end = map(int, input().split())
    segments[i] = [start, end]

segments.sort()  # сортируем массив отрезков
union_segments = [segments[0]]  # массив объединенных отрезков
# проходим по массиву отрезков, если пересекается отрезок с последним в union_segments - объединяем, иначе добавляем в union_segments
for i in range(1, N):
    if segments[i][0] <= union_segments[-1][1]:
        union_segments[-1][1] = max(union_segments[-1][1], segments[i][1])
    else:
        union_segments.append(segments[i])
# ответ - сумма длин окрашенных частей
print(sum([end - start for start, end in union_segments]))
