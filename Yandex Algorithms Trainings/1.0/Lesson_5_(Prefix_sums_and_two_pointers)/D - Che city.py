# считываем данные
n, r = map(int, input().split())  # количество памятников, максимальное расстояние
distances = list(map(int, input().split()))  # отсортированное расстояния между памятниками

# заменим координаты памятников на префиксное расстояние (от первого памятника)
cur = distances[0]
distances[0] = 0
for i in range(1, n):
    cur, distances[i] = distances[i], distances[i] - cur + distances[i - 1]

answer = 0  # ответ
lf = 0  # левая граница окна
# проходим праввой границей окна по массиву
for rg in range(n):
    # если расстояние между памятниками > r, тогда между дальними памятниками тоже > r, увеличиваем answer на n - rg
    if distances[rg] - distances[lf] > r:
        answer += n - rg

        # если вышли за границы расстояния - сдвигаем левый указатель и подсчитываем ответ
        while distances[rg] - distances[lf] > r and lf < rg:
            lf += 1
            # если расстояние между памятниками > r, тогда между дальними памятниками тоже > r поэтому answer += n - rg
            if distances[rg] - distances[lf] > r:
                answer += n - rg
# ответ
print(answer)