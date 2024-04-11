def search_height(lf, rg, volume, volume_lf, volume_rg, x, y):
    """
    Функция поиска максимальной высоты столба воды
    :param lf: левый индекс вершины ломаной
    :param rg: правый индекс вершины ломаной
    :param volume: распределяем внутри объем воды
    :param volume_lf: уже имеемый объем воды слева от l
    :param volume_rg: уже имеемый объем воды справа от r
    :param x: массив координат x точек ломаной
    :param y: массив координат y точек ломаной 
    :return: максимальную высоту столба воды между l и r, для заданных объемов volume, volume_lf, volume_rg
    """
    max_y = -10001  # значение высоты для самой высокой точки
    max_i = -1  # значение индекса в массиве вершин для самой высокой вершины
    for i in range(lf+1, rg):  # проходим по массиву вершин
        if (y[i] > y[i-1]) and (y[i] > y[i+1]):  # если текущая точка является пиком
            if y[i] > max_y:  # обновляем индекс_макс и макс значения
                max_y = y[i]
                max_i = i
    if max_i == -1:  # если пиков не нашли, тогда
        # возвращаем max y - min y
        return binary_search(lf, rg, volume + volume_lf + volume_rg, x, y) - search_min_y(lf, rg, y)
    # если нашли пик
    pos_vol_lf = search_volume(lf, max_i, max_y, x, y)  # считаем возможный вмещаемый объем слева от пика
    pos_vol_rg = search_volume(max_i, rg, max_y, x, y)  # cчитаем возможный вмещаемый объем справа от пика
    inc_vol_lf = (x[max_i] - x[lf]) / (x[rg] - x[lf]) * volume  # считаем объем приходящийся на левую часть при горизонтальном рельефе
    inc_vol_rg = (x[rg] - x[max_i]) / (x[rg] - x[lf]) * volume  # считаем объем приходящийся на правую часть при горизонтальном рельефе

    if (pos_vol_lf > inc_vol_lf + volume_lf - eps) and (pos_vol_rg > inc_vol_rg + volume_rg - eps):  # если нет переполнения воды
        h_lf = search_height(lf, max_i, inc_vol_lf, volume_lf, 0, x, y)  # считаем высоту столба воды слева
        h_rg = search_height(max_i, rg, inc_vol_rg, 0, volume_rg, x, y)  # считаем высоту столба воды справа
        if h_lf > h_rg:  # возвращем больший h
            return h_lf
        else:
            return h_rg
    if (pos_vol_lf > inc_vol_lf + volume_lf) and (pos_vol_rg < inc_vol_rg + volume_rg):  # если есть переполнение уровня воды справа
        if (pos_vol_lf + pos_vol_rg > inc_vol_lf + inc_vol_rg + volume_lf + volume_rg):  # и если нет переполнения уровня воды слева
            h_lf = search_height(lf, max_i, inc_vol_lf, volume_lf, volume_rg + inc_vol_rg - pos_vol_rg, x, y)  # считаем высоту столба воды слева
            h_rg = max_y - search_min_y(max_i, rg, y)  # считаем высоту столба воды справа
            if h_lf > h_rg:  # возвращем больший h
                return h_lf
            else:
                return h_rg
        # если есть переполнение уровня воды и слева, поднимаем общий уровень
        return binary_search(lf, rg, volume + volume_lf + volume_rg, x, y) - search_min_y(lf, rg, y)  # возвращаем max y - min y
    if (pos_vol_lf < inc_vol_lf + volume_lf) and (pos_vol_rg > inc_vol_rg + volume_rg):  # если есть переполнение уровня воды слева
        if (pos_vol_lf + pos_vol_rg > inc_vol_lf + inc_vol_rg + volume_rg + volume_lf):  # и если нет переполнения уровня воды справа
            h_lf = max_y - search_min_y(lf, max_i, y)  # считаем высоту столба воды слева
            h_rg = search_height(max_i, rg, inc_vol_rg, volume_lf + inc_vol_lf - pos_vol_lf, volume_rg, x, y)  # считаем высоту столба воды справа
            if h_lf > h_rg:  # возвращем больший h
                return h_lf
            else:
                return h_rg
        # если есть переполнение уровня воды и справа, поднимаем общий уровень
        return binary_search(lf, rg, volume + volume_rg + volume_lf, x, y) - search_min_y(lf, rg, y)  # возвращаем max y - min y
    # переполнение уровня воды в обоих частях
    return binary_search(lf, rg, volume + volume_rg + volume_lf, x, y) - search_min_y(lf, rg, y)


def search_min_y(lf, rg, y):  # функция поиска самого минимального y от lf до rg
    cur_min = y[lf]  # текущий минимум
    for i in range(lf, rg+1):
        cur_min = y[i] if y[i] < cur_min else cur_min
    return cur_min


def search_volume(l, r, h_target, x, y):  # функция поиска объема, при заданном верхней границе высоты h_target
    cur_v = 0  # текущий объем
    for i in range(l, r):  # проходим по массиву вершин от l до r
        if (y[i] > h_target) and (y[i+1] > h_target):  # если текущая и следующая точки выше h - продолжаем
            continue
        if (y[i] < h_target) and (y[i+1] < h_target):  # если текущая и следующая точки ниже h - увеличиваем объем
            cur_v += (x[i+1] - x[i]) * (h_target - y[i] + h_target - y[i+1]) / 2
            continue
        # находим x точку пересечения, долива воды
        x_cross = x[i] + (h_target - y[i]) / (y[i+1] - y[i]) * (x[i+1] - x[i])
        if (y[i] < h_target):  # если текущая точка ниже h - увеличиваем объем, доливаем воду от x[i] до x_cross
            cur_v += (x_cross - x[i]) * (h_target - y[i]) / 2
            continue
        # если текущая точка выше h, а следующая ниже h - увеличиваем объем, доливаем воду от x_cross до x[i+1]
        cur_v += (x[i+1] - x_cross) * (h_target - y[i+1]) / 2
    # возвращаем полученный объем
    return cur_v


def binary_search(idx_lf, idx_rg, volume, x, y):
    """
    Функция бинарного поиска верхней границы по y столба воды при заданном объеме
    :param idx_lf: левый индекс вершины ломаной
    :param idx_rg: правый индекс вершины ломаной
    :param volume: распределяемый объем
    :param x: массив координат x точек ломаной
    :param y: массив координат y точек ломаной
    :return: верхнюю границу по y столба воды
    """
    if abs(volume) < eps:
        return search_min_y(idx_lf, idx_rg, y)
    h_lf, h_rg = -2e9, 2e9  # границы бин поиска
    while (h_rg - h_lf) > eps:  # погрешность не сошласть на eps
        h_mid = (h_rg + h_lf) / 2
        if search_volume(idx_lf, idx_rg, h_mid, x, y) < volume:  # если получили объем меньше volume - двигаем h_lf
            h_lf = h_mid
        else:
            h_rg = h_mid
    # возвращаем верхнюю границу по y столба воды
    return h_mid


# считываем данные
with open('input.txt', 'r') as f:
    N, H = map(float, f.readline().split())  # число звеньев ломаной, высота столба вобы при горизонтальном рельефе
    N = int(N)
    x, y = [0] * (N + 1), [0] * (N + 1)  # координаты x, y ломаной
    for i in range(N + 1):
        x[i], y[i] = map(int, f.readline().split())

    volume = (x[-1] - x[0]) * H  # объем воды
    eps = 1e-6  # точность
    max_height = search_height(0, N, volume, 0, 0, x, y)  # максимальная высота столба воды

    # ответ
    print(f'{max_height:.5f}\n')
