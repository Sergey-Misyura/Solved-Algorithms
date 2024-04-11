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
        if check(mid, checkparams): # если орков не меньше, двигаем правую границу на mid
            rg = mid
        else:
            lf = mid + 1
    return lf


def check_target_left(m, checkparams):  # проверка числаорков для левого бин поиска
    count_orcs, sum_orcs = checkparams
    return pref_sums[m + count_orcs - 1] - pref_sums[m - 1] >= sum_orcs  # если орков не меньше, True


# считываем данные
n, m = map(int, input().split())  # количество полков, количество вылазок
regiments = list(map(int, input().split()))  # массив полков
pref_sums = [0] * (n + 1)  # массив преф сумм полков
for i in range(n):  # заполняем преф суммы
    pref_sums[i + 1] = pref_sums[i] + regiments[i]

answer = []  # массив ответа
for _ in range(m):
    count_orcs, sum_orcs = list(map(int, input().split()))  # число полков, сумма орков
    start_index = binSearchLeft(1, len(pref_sums) - count_orcs, check_target_left, (count_orcs, sum_orcs))  # используем левый бин поиск
    if pref_sums[start_index + count_orcs - 1] - pref_sums[start_index - 1] == sum_orcs:  # дополнительная проверка на точную сумму орков
        answer.append(start_index)
    else:  # если сумма не сошлась - ответ -1
        answer.append(-1)
# ответ
print(*answer, sep='\n')
