def extend(rect, d):
    """
    Функция расширения прямоугольной области нахождения
    :param rect: координаты прямоугольника
    :param d: размер расширения
    :return: координаты расширенного прямоугольника
    """
    min_plus, max_plus, min_minus, max_minus = rect
    return [min_plus - d, max_plus + d, min_minus - d, max_minus + d]

def intersect(rect1, rect2):
    """
    Функция пересечения прямоугольников
    :param rect1: координаты прямоугольника 1
    :param rect2: координаты прямоугольника 2
    :return: координаты пересечения прямоугольников
    """
    ans = [max(rect1[0], rect2[0]), min(rect1[1], rect2[1]), max(rect1[2], rect2[2]), min(rect1[3], rect2[3])]
    return ans


# считываем данные
t, d, n = map(int, input().split())  # время пробежки, расстояние до искомой позиции, число периодов пробежки

# позиция наклоненного прямоугольника возможных точек нахождения бегуна
pos_rect = (0, 0, 0, 0)  # min(x+y), max(x+y), min(x-y), max(x-y)

# цикл периодов пробежки
for _ in range(n):
    # расширям прямоугольник на координаты за t шагов
    pos_rect = extend(pos_rect, t)
    nav_x, nav_y = map(int, input().split())  # данные навигатора
    # расширяем координаты навигатора на d
    nav_rect = extend((nav_x + nav_y, nav_x + nav_y, nav_x - nav_y, nav_x - nav_y), d)
    # находим пересечение прямоугольников
    pos_rect = intersect(pos_rect, nav_rect)

# восстанавливаем возможные координаты бегуна
probab_points = []  # массив возможных позиций
# проходим по точкам x + y
for x_plus_y in range(pos_rect[0], pos_rect[1] + 1):
    # проходим по точкам x - y
    for x_minus_y in range(pos_rect[2], pos_rect[3] + 1):
        # если сумма четная, высчитываем координаты точки и добавляем в probab_points
        if (x_plus_y + x_minus_y) % 2 == 0:
            x = (x_plus_y + x_minus_y) // 2
            y = x_plus_y - x
            probab_points.append((x, y))

# ответ
print(len(probab_points))
print('\n'.join([str(a)+' '+str(b) for a, b in probab_points]))
