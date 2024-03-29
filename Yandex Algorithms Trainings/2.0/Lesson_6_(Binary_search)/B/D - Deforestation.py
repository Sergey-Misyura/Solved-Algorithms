def binSearchLeft(lf, rg, check, checkparams):
    """
    Бинарный поиск самого левого вхождения числа
    :param lf: левая граница
    :param rg: правая граница
    :param check: функция проверки
    :param checkparams: параметры функции проверки
    :return: значение, на котором сошелся бинарный поиск
    """
    while lf < rg:
        mid = (lf + rg) // 2
        if check(mid, checkparams):
            rg = mid
        else:
            lf = mid + 1
    return lf


def check_tree_count(mid, checkparams):  # проверка количества срубленных деревьев
    per_day1, rest1, per_day2, rest2, target = checkparams
    periods1 = mid // rest1  # периодов работы первого лесоруба
    periods2 = mid // rest2  # периодов работы второго лесоруба
    # возвращает значение - было ли срублено target деревьев
    return ((per_day1 + per_day2) * mid - periods1 * per_day1 - periods2 * per_day2) >= target

# считываем данные
A, K, B, M, X  = map(int, input().split())  # Деревьев в день первым, № дня отдыха1, деревьев в день вторым, № дня отдыха2, таргет
# бин поиск по ответу
print(binSearchLeft(1, X+1, check_tree_count, (A, K, B, M, X)))
