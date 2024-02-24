# считываем данные
N = int(input().strip())
peaks = []  # массив вершин
for _ in range(N):
    peaks.append(tuple(map(int, input().split())))

M = int(input().strip())
tracks = []  # массив трасс
for _ in range(M):
    a, b = map(int, input().split())
    tracks.append([a-1, b-1])

pref_sum = [0]*N  # префиксная сумма высот подъемов при обходе слева направо
reverse_pref_sum = [0]*N  # префиксная сумма высот при обходе подъемов справа налево

# подсчитываем префиксную сумму высот подъемов при обходе слева направо
for i in range(1, N):
    if peaks[i][1] > peaks[i - 1][1]:
        pref_sum[i] = peaks[i][1] - peaks[i - 1][1]
    pref_sum[i] += pref_sum[i - 1]

# подсчитываем префиксную сумму высот подъемов при обходе справа налево
for i in range(N - 2, -1, -1):
    if peaks[i][1] > peaks[i + 1][1]:
        reverse_pref_sum[i] = peaks[i][1] - peaks[i + 1][1]
    reverse_pref_sum[i] += reverse_pref_sum[i + 1]


# выводим ответ
for track in tracks:
    # в зависимости от направления обхода
    if track[0] <= track[1]:
        # при движении слева направо
        print(pref_sum[track[1]] - pref_sum[track[0]])
        # при движении справа налево
    else:
        print(reverse_pref_sum[track[1]] - reverse_pref_sum[track[0]])