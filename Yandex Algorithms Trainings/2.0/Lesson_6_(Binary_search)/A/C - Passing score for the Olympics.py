def binSearchLeft(lf, rg, check, checkparams):
    """
    Левый бин поиск
    :param lf: левая граница
    :param rg: правая граница
    :param check: функция проверки
    :param checkparams: параметры проверки
    :return: найденное число
    """
    while lf < rg:
        mid = (lf + rg) // 2
        if check(mid, checkparams):
            rg = mid
        else:
            lf = mid + 1
    return lf

def binSearchRight(lf, rg, check, target_places):
    """
    Правый бин поиск
    :param lf: левая граница
    :param rg: правая граница
    :param check: функция проверки
    :param checkparams: параметры проверки
    :return: найденное число
    """
    while lf < rg:
        mid = (lf + rg + 1) // 2
        if check(mid, target_places):
            lf = mid
        else:
            rg = mid - 1
    return lf


def check_score_idx(mid, checkparams):
    """
    Функция проверки балла в массиве, для определения числа прошедших участников
    :param mid: индекс текущего балл
    :param checkparams: искомый балл, массив баллов
    :return: возвращает bool больше или равен искомый балл текущему?
    """
    target_score, arr_scores = checkparams  # искомый балл, массив баллов
    return target_score >= arr_scores[mid]


def check_score(mid, target_places):
    """
    Функция проверки минимального проходного балла
    :param mid: проверяемое значение балла
    :param target_places: искомое количество мест
    :return: bool найденные количество мест меньше или равно искомому?
    """
    places = 0  # найденное количество мест
    # ищем количество прошедших по mid баллу участников в all_scores
    idx_in_all = binSearchRight(0, len(all_scores) - 1, check_score_idx, (mid, all_scores))
    places += len(all_scores) - idx_in_all  # увеличиваем places
    if all_scores[idx_in_all] < mid:  # проверяем граничные случаи бин поиска
        places -= 1
    if len(max_region_score) > 0:  # для регионов без финалистов
        # ищем количество прошедших по mid баллу участников с максимальным баллом в регионе
        idx_in_max_region = binSearchRight(0, len(max_region_score) - 1, check_score_idx, (mid, max_region_score))
        places += idx_in_max_region + 1  # увеличиваем places
        if max_region_score[idx_in_max_region] >= mid:  # проверяем граничные случаи бин поиска
            places -= 1

    return places <= target_places

# считываем данные
N, M, R = map(int, input().split())  # число участников первого тура, максимально возможное число участников второго тура и число регионов
winners_count = 0  # количество прошлых финалистов
reg_no_win = set()  # регионы без финалистов
reg_with_win = set()  # регионы с финалистами
max_region_score = dict()  # словарь максимальных баллов для регионов без финалистов
all_scores = []  # массив всех баллов БЕЗ финалистов

for _ in range(N):
    palyer_id, region, score, winner = map(int, input().split())  # id участника, регион, балл, флаг финалиста
    if winner == 1:  # если участник был финалистом
        winners_count += 1  # увеличиваем winners_count
        reg_with_win.add(region)  # добавляем регион в регионы с финалистами
        if region in reg_no_win:  # если регион находится в множестве reg_no_win
            reg_no_win.remove(region)  # удаляем регион
            max_region_score.pop(region)  # удаляем максимальный балл по региону в max_region_score
    else:  # если участник не был финалистом
        if region not in reg_with_win:  # если регион не в регионах с финалистами
            if region not in reg_no_win:  # если регион встретился впервые
                reg_no_win.add(region)  # добавляем регион в reg_no_win
                max_region_score[region] = score  # добавляем макс значение по региону в max_region_score
            else:  # иначе, обновляем max_region_score
                max_region_score[region] = max(score, max_region_score[region])

        all_scores.append(score)  # добавляем баллы ко всем баллам

all_scores.sort()  # сортируем
max_region_score = sorted(list(max_region_score.values()))  # сохраняем только максимальные значения регионов и сортируем
answer = 0  # переменная ответа
if M > winners_count:  # если число место меньше числа прошлых финалистов - ищем мин проходной бал бин поиском
    answer = binSearchLeft(0, all_scores[-1]+1, check_score, M - winners_count)
else:  # если финалистов столько сколько мест
    if all_scores:  # и есть кто-то помимо финалистов
        answer = all_scores[-1] + 1  # устанавливаем балл выше максимального балла не_финалиста

# ответ
print(answer)