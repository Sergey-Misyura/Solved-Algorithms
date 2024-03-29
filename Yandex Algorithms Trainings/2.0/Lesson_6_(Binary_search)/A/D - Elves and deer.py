def groups(count, deers, elves):
    """
    Функция моделирование групп
    :param count: количество используемых пар эльфов
    :param deers: список оленей
    :param elves: список эльфов
    :return: bool - получилось ли создать группу по используемым парам; группы эльфов и оленей
    """
    cur_deer = 0  # индекс текущего оленя
    answer = []  # массив групп
    # проходим по левым эльфам в группах
    for lf_elf in range(count):
        rg_elf = len(elves) - count + lf_elf  # индекс правого эльфа в группе
        # пока олени левее левого эльфа - пропускаем
        while cur_deer < len(deers) and deers[cur_deer][0] <= elves[lf_elf][0]:
            cur_deer += 1
        # если оленей не осталось или очередной правее правого эльфа - ответ False
        if cur_deer == len(deers) or deers[cur_deer][0] >= elves[rg_elf][0]:
            return False, []
        # добавляем к ответу группу (олень, эльфы)
        answer.append((deers[cur_deer][1], elves[lf_elf][1], elves[rg_elf][1]))
        cur_deer += 1  # следующий олень
    # возвращаем флаг и ответ
    return True, answer


# считываем данные
m, n = map(int, input().split())  # количество оленей и эльфов
deers = [(deer, i + 1) for i, deer in enumerate(list(map(int, input().split())))]  # массив пронумерованных оленей
elves = [(elf, i + 1) for i, elf in enumerate(list(map(int, input().split())))]  # массив пронумерованных эльфов
# сортируем массивы
deers.sort()
elves.sort()

# правый бин поиск
lf, rg = 0, min(m, n // 2)  # левый, правый указатели
while lf < rg:
    mid = (lf + rg + 1) // 2  # количество используемых пар
    groups_flag, ans = groups(mid, deers, elves)  # проверяем mid
    # если удалось создать mid команд - двигаем lf к mid, иначе rg к mid - 1
    if groups_flag:
        lf = mid
    else:
        rg = mid - 1
# ответ
print(lf)  # количество команд
_, ans = groups(lf, deers, elves)
for team in ans:
    print(*team)  # команды эльфов и оленей
