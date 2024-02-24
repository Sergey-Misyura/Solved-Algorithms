def to_minutes(time):
    """
    Функция перевода часов:минут в минуты
    :param time: время, часов:минут
    :return: минуты
    """
    h, m = time.split(':')
    return int(h) * 60 + int(m)


# считываем данные
N, M = map(int, input().split())  # городов, рейсов
count_buses = [0] * (N + 1)  # количество автобусов в каждом городе
bus_balance = [0] * (N + 1)  # баланс автобусов в городе
events = []  # массив событий
overmidnight = 0  # количество рейсов через полночь
# добавляем данные в events и считаем баланс
for i in range(M):
    # город отправления, время отправления, город прибытия, время прибытия
    city_dep, dep_time, city_arr, arr_time = input().split()
    city_dep = int(city_dep)
    city_arr = int(city_arr)
    dep_time = to_minutes(dep_time)
    arr_time = to_minutes(arr_time)
    # при полуночном рейсе увеличиваем счетчик рейсов overmidnight
    if arr_time < dep_time:
        overmidnight += 1
    # обновляем баланс автобусов в городе
    bus_balance[city_dep] -= 1
    bus_balance[city_arr] += 1
    # добавляем в events
    events.append((dep_time, 1, city_dep))
    events.append((arr_time, -1, city_arr))


disbalance = False  # флаг дисбаланса автобусов
# проверяем баланс автобусов, если его нет, тогда автобусы либо бесконечно копятся или исчезают, флаг дисбаланса True
for i in range(N + 1):
    if bus_balance[i] != 0:
        disbalance = True
# если дисбаланс - выводим -1
if disbalance:
    print(-1)
# иначе, если баланс сохраняется
else:
    # сортируем события
    events.sort()
    # проходим по событиям вevents
    for event in events:
        # если автобус приехал, увеличиваем счетчик в городе прибытия
        if event[1] == -1:
            count_buses[event[2]] += 1
        # иначе, автобус уехал и если есть свободные автобусы, отправляем автобус в рейс, уменьшаем счетчик
        # если свободных автобусов нет и у нас сохранялся баланс, значит это полуночный рейс,
        # который учтется на следующие сутки, ничего не изменяем
        else:
            if count_buses[event[2]] > 0:
                count_buses[event[2]] -= 1
    # суммируем число автобусов в городах
    answer = sum(count_buses)  # ответ

    # к ответу добавляем автобусы, находящиеся в пути, проходящие в полуночное время
    print(answer + overmidnight)
