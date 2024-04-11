# также переписан на cpp

def binSearchLeft(lf, rg, check):  # левый бин поиск
    while lf < rg:
        mid = (lf + rg) // 2
        if check(mid):
            rg = mid
        else:
            lf = mid + 1
    return lf


def check_tiles(width):  # функция проверки покрытости плитки
    last_in = 0  # правый край раздвижного окна
    for i in range(len(tiles)):  # проходим левым краем окна по плитке
        while last_in < n - 1 and tiles[last_in + 1] <= tiles[i] + width - 1:  # двигаем правый край по ширине окна
            last_in += 1
        if last_in == n - 1:  # если правым краем дошли до конца
            if i != 0:  # и если левый край окна не первая плитка
                min_y, max_y = pref_min_y[i], pref_max_y[i]  # получаем min max y координаты из префикса
            else:  # иначе покрыли - ответ True
                return True
        elif i != 0:  # иначе, если плитка не первая, получаем min max y координаты сравнивая префиксы и суффиксы
            min_y = min(pref_min_y[i], suf_min_y[last_in + 1])
            max_y = max(pref_max_y[i], suf_max_y[last_in + 1])
        else:  # иначе, если i == 0 получаем min max y координаты из суффикса
            min_y, max_y = suf_min_y[last_in + 1], suf_max_y[last_in + 1]

        if max_y - min_y <= width - 1:  # если покрыли y - ответ True
            return True

    return False

# считываем данные
with open('input.txt', 'r') as f:
    w, h, n = map(int, f.readline().split())  # ширина и высота площади и количество потрескавшихся плиток
    tiles = [0] * n  # массив координат плиток
    for i in range(n):
        tiles[i] = list(map(int, f.readline().split()))

tiles.sort()  # сортируем плитку
pref_min_y = [float('inf')] * (n + 1)  # массив префиксных минимумов по y координате
pref_max_y = [float('-inf')] * (n + 1)  # массив префиксных максимумов по y координате
suf_min_y = [float('inf')] * (n + 1)  # массив суффиксных минимумов по y координате
suf_max_y = [float('-inf')] * (n + 1)  # массив суффиксных максимумов по y координате
# заполняем массивы y суффиксов и префиксов
for i in range(n):
    pref_min_y[i + 1] = min(pref_min_y[i], tiles[i][1])
for i in range(n):
    pref_max_y[i + 1] = max(pref_max_y[i], tiles[i][1])
for i in range(n - 1, -1, -1):
    suf_min_y[i] = min(suf_min_y[i + 1], tiles[i][1])
for i in range(n - 1, -1, -1):
    suf_max_y[i] = max(suf_max_y[i + 1], tiles[i][1])

tiles = [x for x, _ in tiles]  # оставляем только x координату
answer = binSearchLeft(1, max(w, h), check_tiles)  # ищем ответ левым бинпоиском по ответу

# ответ
print(answer)
