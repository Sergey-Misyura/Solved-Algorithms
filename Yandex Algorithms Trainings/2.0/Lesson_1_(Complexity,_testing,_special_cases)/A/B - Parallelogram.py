def IsPointsOnLine(x1, y1, x2, y2, x3, y3):
    """
    Функция, проверяющая находятся ли 3 точки на 1 прямой
    :param x1: x первой точки
    :param y1: y первой точки
    :param x2: х второй точки
    :param y2: y второй точки
    :param x3: х третьей точки
    :param y3: y третьей точки
    :return: True если находятся
    """

    return (x3 * (y2 - y1) - y3 * (x2 - x1) == x1 * y2 - x2 * y1)


# считываем данные
N = int(input().strip())  # число коэффициентов
for _ in range(N):
    coords_seq = list(map(int, input().split()))
    coords = []  # массив координат
    for i in range(0, 8, 2):
        x = coords_seq[i]
        y = coords_seq[i + 1]
        coords.append((x, y))

    is_parallelogram = True  # флаг параллелограмма
    # если точки дублируется - это не параллелограмм
    if len(set(coords)) != 4:
        is_parallelogram = False

    # проверка лежачих на одной прямой 3 точек, если лежат - это не параллелограмм
    for i in range(4):
        for j in range(i+1, 4):
            for k in range(j+1, 4):
                if IsPointsOnLine(coords[i][0], coords[i][1], coords[j][0], coords[j][1], coords[k][0], coords[k][1]):
                    is_parallelogram = False
                    break

    # базовый случай
    if is_parallelogram:
        # сортируем координаты по х
        coords.sort()
        # проверяем попарно стороны, зафиксировав первую и последнюю точки массива (стороны между 1-2 и 3-4, 1-3 и 2-4 точками)
        for i in range(1, 3):
            # для случая если делить обращается в 0 при x1 == x2 и x3 == x4 (в таком случае стороны параллельны)
            if coords[0][0] == coords[i][0] and coords[3 - i][0] == coords[3][0]:
                # если длина сторон разная - не парраллелограмм
                if (coords[i][0]-coords[0][0])**2 != (coords[3 - i][0]-coords[3][0])**2:
                    is_parallelogram = False
            # иначе если координаты x точек одной стороны равны, а x другой стороны не равны - не парраллелограмм
            elif coords[0][0] == coords[i][0]:
                is_parallelogram = False
            elif coords[3 - i][0] == coords[3][0]:
                is_parallelogram = False
            # проверяем равнество уравнений прямых y = kx+b, как k1 = (y0 - y1) / (x0 - x1), k2 = (y2 - y2) / (x2 - x3)
            # k1 == k2 => (y0 - y1)*(x2 - x3)==(y2 - y2)*(x0 - x1)
            else:
                dy1 = (coords[0][1] - coords[i][1])
                dx1 = (coords[0][0] - coords[i][0])
                dy2 = (coords[3 - i][1] - coords[3][1])
                dx2 = (coords[3 - i][0] - coords[3][0])
                if dy1 * dx2 != dy2 * dx1:
                    is_parallelogram = False

    # ответ
    if is_parallelogram:
        print('YES')
    else:
        print('NO')