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

def binSearchRight(lf, rg, check, checkparams):
    """
    Бинарный поиск самого правого вхождения числа
    :param lf: левая граница
    :param rg: правая граница
    :param check: функция проверки
    :param checkparams: параметры функции проверки
    :return: значение, на котором сошелся бинарный поиск
    """
    while lf < rg:
        mid = (lf + rg + 1) // 2
        if check(mid, checkparams):
            lf = mid
        else:
            rg = mid - 1
    return lf

def check_target_left(m, target):  # проверка для левого бин поиска
    return target <= nums[m]


def check_target_right(m, target):  # проверка для правого бин поиска
    return target >= nums[m]

# считываем данные
N = int(input().strip())  # количество чисел в массиве
nums = list(map(int, input().split()))  # массив чисел
M = int(input().strip())  # количество запросов
reqs = list(map(int, input().split()))  # массив запросов

nums.sort()  # сортируем массив
answer = [0] * M  # массив ответа
for i in range(M):
    # находим левый и правый индекс искомого числа
    lf_idx = binSearchLeft(0, len(nums) - 1, check_target_left, reqs[i])
    rg_idx = binSearchRight(0, len(nums) - 1, check_target_right, reqs[i])
    # если числа нет в массиве по найденным индексам - записываем в ответ 0 0
    if nums[lf_idx] != reqs[i]:
        answer[i] = '0 0'
    else:
        answer[i] = str(lf_idx + 1) + ' ' + str(rg_idx + 1)

# ответ
print(*answer, sep='\n')