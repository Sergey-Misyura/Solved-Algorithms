def check_brigs(max_discomfort, checkparams):
    """
    Функция - проверяет возможность создания числа бригад не меньше требуемого, при дискомфорте не больше заданного
    :param max_discomfort: максимальное неудобство
    :param checkparams: (минимальное число бригад, количество людей в бригаде, рост всех людей)
    :return: возвращаем True если набрали требуемое число бригад
    """
    min_brig, people_in_brig, heights = checkparams  # минимальное число бригад, количество людей в бригаде, рост людей
    human_idx = 0  # номер очередного человека
    brigades = 0  # текущее число бригад
    # пока не вышли за пределы массива, набираем жадно бригады с числом неудобства не более max_discomfort
    while human_idx < len(heights) - people_in_brig + 1:
        # если текущее значение неудоства нам подходит, то добавляем бригаду и сдвигаем указатель на количество людей в бригаде
        if heights[human_idx + people_in_brig - 1] - heights[human_idx] <= max_discomfort:
            brigades += 1
            human_idx += people_in_brig
        # иначе сдвигаем указатель очередного человека на 1
        else:
            human_idx += 1

    # сравниваем полученное число бригад с необходимым
    return brigades >= min_brig

# левый бин поиск
def left_bin_search(lf, rg, check, checkparams):
    while lf < rg:
        mid = (lf + rg) // 2
        if check(mid, checkparams):
            rg = mid
        else:
            lf = mid + 1
    return lf

N, R, C = map(int, input().split())  #  число человек в классе, минимально необходимое число бригад, человек в каждой бригаде
heights = []  # рост участников
for _ in range(N):
    heights.append(int(input().strip()))

# сортируем
heights.sort()
# бин поиск минимального дискомфорта по ответу: от 0 до макс разницы в росте
print(left_bin_search(0, heights[-1] - heights[0], check_brigs, (R, C, heights)))