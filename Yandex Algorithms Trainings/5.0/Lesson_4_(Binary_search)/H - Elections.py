def get_count_votes(cur_idx, voters, suffix_sum, level):
    """
    Функция подсчета получаемых голосов при срезе
    :param cur_idx: партия для которой считаем получаемые голоса
    :param voters: массив голосующих
    :param suffix_sum: массив суффиксных сумм
    :param level: уровень среза голосов
    :return: получаемые при срезе голоса
    """
    lf, rg = 0, len(voters) - 1  # границы бин поиска
    # находим партию самую близкую к level, для подсчета голосов от нее и вправо
    while lf < rg:
        mid = (lf + rg) // 2  # индекс текущей партии для бин поиска
        if voters[mid][0] < level:
            lf = mid + 1
        else:
            rg = mid
    if voters[lf][0] < level:  # если level слишком большой - возвращаем 0
        return 0
    count_votes = suffix_sum[lf] - level * (len(voters) - lf)  # подсчитываем получаемые голоса исходя из партии lf
    if voters[cur_idx][0] >= level:  # если партия для которой считаем >= level, убираем срезанные с нее голоса
        count_votes -= (voters[cur_idx][0] - level)
    # возвращаем получаемые при срезе голоса
    return count_votes


def cost_calculation(voters, cur_idx, suffix_sum):
    """
    Функция моделирования перераспределения голосов
    :param voters: отсортированный массив голосующих избирателей
    :param cur_idx: проверяемая партия в массиве voters
    :param suffix_sum: массив суффиксных сумм
    :return: количество/стоимость полученных голосов, уровень среза голосов, количество возвращаемых голосов
    """
    lf, rg = 0, 10 ** 6  # границы бин поиска уровня среза
    while lf < rg:
        level = (lf + rg + 1) // 2  # уровень среза голосов
        count_votes = get_count_votes(cur_idx, voters, suffix_sum, level)  # количество получаемых голосов
        # если итогавая сумма больше уровня - сдвигаем левую границу уровня, иначе правую на level - 1
        if count_votes + voters[cur_idx][0] > level:
            lf = level
        else:
            rg = level - 1
    count_votes = get_count_votes(cur_idx, voters, suffix_sum, lf)  # пересчитываем count_votes
    recovery = max(0, voters[cur_idx][0] + count_votes - lf - 2)  # подсчитываем количество возвращаемых голосов
    return count_votes - recovery, lf, recovery


# считываем данные
n = int(input().strip())  # количество партий
payoff = [0] * n  # массив взяток для партий
voters = [0] * n  # массив жителей, которые собираются проголосовать за i партию
for i in range(n):  # проходим по массиву голосующих
    v, payoff[i] = map(int, input().split())  # голосов, взятка
    voters[i] = (v, i)  # количество голосующих жителей за партию, номер партии

# сортируем массив voters по возрастанию голосов и подсчитываем суффиксные суммы
voters.sort()
suffix_sum = [0] * n  # массив суффиксных сумм по голосам
suffix_sum[-1] = voters[-1][0]
for i in range(n - 2, -1, -1):  # проходим с конца по голосам
    suffix_sum[i] = suffix_sum[i + 1] + voters[i][0]  # обновляем массив суффиксных сумм

# перебор подходящих партий
min_cost = 10 ** 6 + 10 ** 6 * 10 ** 6 + 1  # минимальные затраты на покупку голосов и взятку
for cur_idx in range(n):  # проходим по массиву голосующих
    if payoff[voters[cur_idx][1]] != -1:  # если партию можно подкупить
        cur_cost, level, recovery = cost_calculation(voters, cur_idx, suffix_sum)  # стоимость, уровень среза, количество возвращаемых голосов
        if payoff[voters[cur_idx][1]] + cur_cost < min_cost:  # если взятка + стоимость < мин стоимость - обновляем min_cost и ответ
            min_cost = payoff[voters[cur_idx][1]] + cur_cost
            answer = [cur_idx, cur_cost, level, recovery]


# восстановление ответа
winner, cost, level, recovery = answer  # индекс номер победителя, стоимость, уровень среза, количество возвращаемых голосов
res_votes = [0] * n  # массив результатов голосования
for cur_idx in range(n):  # проходим по массиву голосующих
    if cur_idx == winner:  # если нашли индекс номер победителя, записываем результат победы
        res_votes[voters[cur_idx][1]] = voters[cur_idx][0] + cost
    elif voters[cur_idx][0] <= level:  # иначе, если нашли партию с голосами меньше среза - добавляем ее голоса в res_votes
        res_votes[voters[cur_idx][1]] = voters[cur_idx][0]
    else:  # иначе, если нашли партию у которой убирали голоса, при recovery > 0 возвращаем 1 голос, уменьшаем recovery
        if recovery > 0:
            res_votes[voters[cur_idx][1]] = level + 1
            recovery -= 1
        else:  # если recovery 0, оставляем в res_votes у партии значение среза
            res_votes[voters[cur_idx][1]] = level

# ответ
print(min_cost)  # минимальные затраты
print(voters[winner][1] + 1)  # номер партии, которой дается взятка
print(*res_votes)  # количество голосов, которые будут отданы за каждую из партий после осуществления операции