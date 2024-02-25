# считываем данные
buildings = list(map(int, input().split()))  # массив зданий
houses = set()  # множество индексов домов
shops = set()  # множество индексов магазинов

# добавляем индексы в houses и shops
for i, build in enumerate(buildings):
    if build == 1:
        houses.add(i)
    elif build == 2:
        shops.add(i)

max_min_dist = -1  # максимальная среди всех дистанция от дома до ближайшего магазина
# проходим по домам
for house in houses:
    # считаем дистанцию от дома до ближайшего магазина
    cur_min_dist = min([abs(house - shop) for shop in shops])
    # обновляем максимальную среди всех дистанцию от дома до магазина
    max_min_dist = max(max_min_dist, cur_min_dist)

# ответ
print(max_min_dist)