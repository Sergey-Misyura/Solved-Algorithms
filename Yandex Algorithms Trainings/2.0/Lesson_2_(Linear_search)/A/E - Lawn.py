from math import floor, ceil
# считываем данные
x1, y1, x2, y2 = map(int, input().split())  # координаты постриженного участка
x_sprinkler, y_sprinkler, r = map(int, input().split())  # координаты и радиус дождевальной установки

x1, x2 = min(x1, x2), max(x1, x2)  # упорядочиваем x
y1, y2 = min(y1, y2), max(y1, y2)  # упорядочиваем y

answer = 0  # переменная ответа
# проходим по y координатам пересечения участка и радиуса действия установки
for y in range(max(y1, y_sprinkler - r), min(y2, y_sprinkler + r) + 1):
    # считаем дальность действия установки по x от текущего y
    dx = (r**2 - (y - y_sprinkler)**2) ** 0.5
    # для текущего y находим координаты х пересчения радиуса действия установки с участком
    max_x = min(x2, floor(x_sprinkler + dx))
    min_x = max(x1, ceil(x_sprinkler - dx))
    # если координаты образуют отрезок - увеличиваем ответ
    if max_x >= min_x:
        answer += max_x - min_x + 1
# ответ
print(answer)