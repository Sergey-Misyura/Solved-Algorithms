from collections import defaultdict


def is_winner(grid, player):
    """
    Функция проверки игрока на победу
    :param grid: сетка крестики-нолики
    :param player: номер игрока
    :return: решение о победе указанного игрока
    """
    winner = False  # переменная победы игрока
    # проверка каждой строки на заполненность знаками игрока, если все 3 записаны - флаг True
    for row in grid:
        if all(num == player for num in row):
            winner = True
    # если не нашли победителя
    if not winner:
        # проверка каждого столбца на заполненность знаками игрока, если все 3 записаны - флаг True
        for col in range(3):
            if all(num == player for num in (grid[0][col], grid[1][col], grid[2][col])):
                winner = True
    # если не нашли победителя
    if not winner:
        # проверка диагоналей сетки на заполненность знаками игрока, если все 3 записаны - флаг True
        if all(num == player for num in (grid[0][0], grid[1][1], grid[2][2])) \
                or all(num == player for num in (grid[0][2], grid[1][1], grid[2][0])):
            winner = True
    # возвращаем решение о победе указанного игрока
    return winner


num_dict = defaultdict(int)  # счетчик крестиков и ноликов
grid = []  # сетка
# считываем данные
for _ in range(3):
    row = list(map(int, input().split()))
    grid.append(row)
    # добавляем в счетчик
    for num in row:
        num_dict[num] += 1
diff = num_dict[1] - num_dict[2]  # разница между крестиками и ноликами
# если разницы нет или в единицу
if diff == 0 or diff == 1:
    # проверка первого игрока на победу
    first_win = is_winner(grid, 1)
    # проверка второго игрока на победу
    second_win = is_winner(grid, 2)
    # если оба победили - ответ NO
    if first_win and second_win:
        print('NO')
    # если после победы первого, второй сделал ход - ответ NO
    elif first_win and diff == 0:
        print('NO')
    # если после победы второго, первый сделал ход - ответ NO
    elif second_win and diff == 1:
        print('NO')
    # иначе все правильно - ответ YES
    else:
        print('YES')
# если разница выше - ответ NO
else:
    print('NO')
