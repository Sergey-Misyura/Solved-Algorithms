import math


def search_time(lf, rg, eps, check):  # бин поиск макс времени достижения мяча противником
    x_target, y_target = 0, 0  # начальные значения искомых координат мяча
    while rg - lf > 2 * eps:  # продолжаем пока превышаем точность
        mid = (lf + rg) / 2
        can_hit, x, y = check(mid)
        if can_hit:  # если мяч достигается не меньше чем за mid - сдвигаем левую границу, сохраняем координаты мяча
            lf = mid
            x_target, y_target = x, y
        else:
            rg = mid
    # возвращаем время и координаты
    return lf, x_target, y_target


def get_intersections(x0, y0, r0, x1, y1, r1):
    """
    Функция проверки и нахождения точек пересечения двух окружностей
    :param x0: x центра первой окружности
    :param y0: y центра первой окружности
    :param r0: радиус первой окружности
    :param x1: x центра второй окружности
    :param y1: y центра второй окружности
    :param r1: радиус второй окружности
    :return: точки пересечения, либо None если их нет
    """
    d = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)  # считаем расстояние
    if d > r0 + r1:  # если расстояние больше суммы радиусов - окружности не пересекаются, ответ None
        return None
    if d < abs(r0 - r1):  # если один круг внутри другого - ответ None
        return None
    if d == 0 and r0 == r1:  # если круги совпадают - ответ None
        return None
    else:  # иначе считаем точки пересечения
        a = (r0 ** 2 - r1 ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(r0 ** 2 - a ** 2)
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d
        x3 = x2 + h * (y1 - y0) / d
        y3 = y2 - h * (x1 - x0) / d
        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d
        # возвращаем массив точек пересечения, если точка одна - будет дубироваться
        return (x3, y3, x4, y4)


def try_time(time):  # функция проверки времени достижения мяча противником и нахождения target координат мяча
    possible_points = {(0, D), (0, 0), (-D, 0), (D, 0)}  # возможные точки отправки мяча
    for x, y, v in opponents:  # добавляем точки пересечения окружностей противников с верхней полуокружностью (0, 0, D)
        r = v * time  # радиус
        intersect = get_intersections(0, 0, D, x, y, r)
        if intersect:  # если есть пересечение
            x1, y1, x2, y2 = intersect  # получаем координаты
            if y1 >= 0:  # добавляем первую точку при y не меньше 0
                possible_points.add((x1, y1))
            if y2 >= 0:  # добавляем вторую точку при y не меньше 0
                possible_points.add((x2, y2))
        # добавляем точки пересечения окружностей c диаметром (0, 0, D) - отрезком x = [-D, D], y = 0
        if r == y and -D <= x <= D:  # при одной точке пересечения с отрезком
            possible_points.add((x, 0))
        elif r > y:  # если две точки пересечения, считаем нижний катет прямоугольного треугольника
            dx = math.sqrt(r ** 2 + y ** 2)
            if -D <= x - dx <= D:  # если левая точка лежит на отрезке - добавляем
                possible_points.add((x - dx, 0))
            if -D <= x + dx <= D:  # если правая точка лежит на отрезке - добавляем
                possible_points.add((x + dx, 0))
    for i in range(N - 1):  # добавляем в множество точки пересечений между собой окружностей противников
        for j in range(i + 1, N):
            x1, y1, v1 = opponents[i]  # первый противник
            x2, y2, v2 = opponents[j]  # второй противник
            intersect = get_intersections(x1, y1, v1 * time, x2, y2, v2 * time)
            if intersect:  # если есть пересечение
                x3, y3, x4, y4 = intersect  # получаем координаты
                if y3 >= 0 and x3 ** 2 + y3 ** 2 <= D ** 2:  # добавляем первую точку при y не меньше 0
                    possible_points.add((x3, y3))
                if y4 >= 0 and x4 ** 2 + y4 ** 2 <= D ** 2:  # добавляем вторую точку при y не меньше 0
                    possible_points.add((x4, y4))

    for point in possible_points:  # проверка точек на достижимость соперником не раньше чем за time
        reachable_in_time = True  # флаг достижимости не раньше чем за time
        for x, y, v in opponents:  # проходим по противникам
            # если полученное расстояние от меча до противника < скорость * время, то есть он прибежит быстрее
            if round((point[0] - x) ** 2 + (point[1] - y) ** 2, 4) < round((v * time) ** 2, 4):
                reachable_in_time = False  # меняем флаг на False, останавливаемся
                break
        if reachable_in_time:  # если ни один противник раньше не прибегает, тогда возвращаем True, координаты точки
            return True, point[0], point[1]
    # при достижении мяча раньше time - возвращаем False, 0, 0
    return False, 0, 0


# считываем данные
D, N = map(int, input().split())  # максимальное расстояние удара и количество соперников на поле
opponents = [0] * N  # массив координат соперников
for i in range(N):
    opponents[i] = list(map(int, input().split()))
eps = 0.0001  # точность

# находим правую границу бин поиска
max_time = float('-inf')  # максимальное время достижения мяча
for x, y, v in opponents:
    max_time = max(max_time, ((x + D) ** 2 + y ** 2) ** 0.5 / v)
    max_time = max(max_time, ((x - D) ** 2 + y ** 2) ** 0.5 / v)

time_target, x_target, y_target = search_time(0, max_time, eps,
                                              try_time)  # бин поиск по ответу: время достижения мяча, координаты

# ответ
print(round(time_target, 4))
print(round(x_target, 4), round(y_target, 4))
