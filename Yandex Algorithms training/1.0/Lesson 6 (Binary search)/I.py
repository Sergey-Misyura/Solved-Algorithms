def check_brigs(max_discomfort, checkparams):
    """
    :param max_discomfort: максимальное неудобство
    :param checkparams: (минимальное число бригад, количество людей в бригаде, рост всех людей)
    :return: возвращаем True если набрали требуемое число бригад
    """
    min_brig, people_in_brig, heights = checkparams
    cur_max_in_brig = 0
    brigades = 0
    # набираем жадно бригады с числом неудобства не более max_discomfort
    while cur_max_in_brig < len(heights) - people_in_brig + 1:
        # если текущее значение неудоства нам подходит, то добавляем бригаду и сдвигаем указатель на количество людей в бригаде
        if heights[cur_max_in_brig + people_in_brig - 1] - heights[cur_max_in_brig] <= max_discomfort:
            brigades += 1
            cur_max_in_brig += people_in_brig
        # иначе сдвигаем указатель на 1
        else:
            cur_max_in_brig += 1

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

N, R, C = map(int, input().split())
heights = []
for _ in range(N):
    heights.append(int(input().strip()))

# сортируем
heights.sort()
# бин поиск по ответу
print(left_bin_search(0, heights[-1] - heights[0], check_brigs, (R, C, heights)))