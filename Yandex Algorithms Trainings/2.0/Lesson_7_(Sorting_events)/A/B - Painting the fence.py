def binSearchRight(lf, rg, check, checkparams):
    while lf < rg:
        mid = (lf + rg + 1) // 2
        if check_coloring(mid, checkparams):  # если укладывается в длину забора - сдвигаем lf на mid
            lf = mid
        else:
            rg = mid - 1
    return lf


def check_coloring(mid, checkparams):  # функция сравнения покрашенных досок с целевой длиной забора
    friend_boards, k = checkparams
    colored = 0  # текущее число покрашеных досок
    for boards in friend_boards:  # проходим по friend_boards, жадно выбираем сколько минимум друзья покарасят при mid
        colored = max(colored + mid, boards)
    return colored <= k

# считываем данные
n, k = map(int, input().split())  # число друзей, длина забора
friend_boards = sorted(list(map(int, input().split())))  # список желаемых красить друзьями досок
# используем правый бин поиск от 0 до друга с наименьшим числом досок
happienes = binSearchRight(0, friend_boards[0], check_coloring, (friend_boards, k))  # удовлетворенность

# ответ
print(happienes)
