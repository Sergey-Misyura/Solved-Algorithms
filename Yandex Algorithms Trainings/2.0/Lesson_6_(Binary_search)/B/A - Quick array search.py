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
N = int(input().strip())  # количество чисел
nums = list(map(int, input().split()))  # массив чисел
nums.sort()  # сортируем массив
K = int(input().strip())  # количество запросов
answer = [0] * K  # массив ответа
for i in range(K):
    L, R = map(int, input().split())  # левая, правая границы поиска
    # если массив не пересекается с граница, оставляем 0
    if nums[0] > R or nums[-1] < L:
        answer[i] = 0
    # иначе находим индекс самого левого и самого правого чисел между L и R, сохраняем в ответ
    else:
        lf_idx = binSearchLeft(0, len(nums) - 1, check_target_left, L)
        rg_idx = binSearchRight(0, len(nums) - 1, check_target_right, R)
        answer[i] = rg_idx - lf_idx + 1

# ответ
print(*answer)