def lbin_search(helpers, target, len_helpers):
    """
    Левый бинарный поиск, для нахождения минимального времени надувания всех шаров
    :param helpers: массив помощников
    :param target: искомое количество шаров
    :param len_helpers: количество помощников
    :return: минимальное время надувания target шаров; массив шаров, надутых каждым человеком
    """
    lf, rg = 0, 200 * 15000  # границы
    while lf < rg:
        mid = (lf + rg) // 2
        total = 0  # общее число надутых шаров
        # проходим по помощникам, считаем общее количество надутых шаров
        for i in range(len_helpers):
            # количество циклов надувания помощником, оставшееся время после последнего цикла
            cycles, rems = divmod(mid, helpers[i][2])
            # добавляем к общему количеству число шаров, надутых помощником
            total += cycles * helpers[i][1] + min(rems // helpers[i][0], helpers[i][1])

        if total < target:
            lf = mid + 1
        else:
            rg = mid

    # после нахождения оптимального времени, из числа target подсчитываем шары надутые каждым помощником
    cur_target = target  # текущее оставшееся количество шаров
    answer = [0] * len_helpers  # ответ
    # проходим по массиву helpers, считаем надутые шары, сохраняем в answer
    # для точного попадания в target используем min(оставшиеся, надутые шары helper[i])
    for i in range(len_helpers):
        cycles, rems = divmod(lf, helpers[i][2])
        answer[i] = min(cur_target, cycles * helpers[i][1] + min(rems // helpers[i][0], helpers[i][1]))
        cur_target -= answer[i]
    # возвращаем минимальное время надувания target шаров; массив шаров, надутых каждым человеком
    return lf, answer


# считываем данные
M, N = map(int, input().split())  # М - воздушных шаров, N - помощников
helpers = [None] * N  # массив помощников

# добпаляем помощников
for i in range(N):
    T, Z, Y = map(int, input().split())
    # сохраняем время надувания шара, количество повторений до отдыха, длину цикла надуваний и отдыха
    helpers[i] = (T, Z, T * Z + Y)

# используем бинарный поиск по ответу
count, count_list = lbin_search(helpers, M, N)  # время надувания всех шариков, количество шаров надутых каждым помощником
print(count)
print(*count_list)
