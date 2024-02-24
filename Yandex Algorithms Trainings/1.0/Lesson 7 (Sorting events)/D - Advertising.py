# считываем данные
N = int(input().strip())  # N - количество покупателей
events = []  # массив событий
for i in range(N):
    a, b = map(int, input().split())
    # добавляем в events, когда покупатель пробыл >= 5 минут
    if b - a >= 5:
        events.append((a, -1, i))
        # уменьшаем вряме ухода на длину рекламы
        events.append((b - 5, 1, i))

# сортировка
events.sort()
# частный случай при 0 человек
if len(events) == 0:
    print(0, 0, 5)
# частный случай при 1 человеке
elif len(events) == 2:
    print(1, events[0][0], events[0][0] + 5)
else:
    best_people = 0  # максимальное общее число людей прослушавших 2 рекламы
    first_ad, second_ad = 0, 0  # время начала реклам
    first_ad_peoples = set()  # люди для первой рекламы
    # проходим по массиву events для первой рекламы
    for i in range(len(events)):
        cur_event = events[i]  # текущее событие
        # если человек пришел
        if cur_event[1] == -1:
            # добавляем человека в множество first_ad_peoples
            first_ad_peoples.add(cur_event[2])
            # обновляем ответ, если найдено больше людей чем в текущем best_people, обновляем время начала реклам
            if len(first_ad_peoples) > best_people:
                best_people = len(first_ad_peoples)
                first_ad = cur_event[0]
                second_ad = cur_event[0] + 5

        # проходим по оставшейся части массива events для второй рекламы
        second_ad_count = 0  # количество людей для второй рекламы
        for j in range(i + 1, len(events)):
            second_event = events[j]  # второе событие
            # если приходит новый человек - увеличиваем счетчик second_ad_count
            if second_event[1] == -1 and second_event[2] not in first_ad_peoples:
                second_ad_count += 1
            # если вторая реклама на расстоянии >= 5 от первой и сумма текущих количеств людей больше best_people -
            # обновляем ответ и время реклам
            if second_event[0] - 5 >= cur_event[0] and len(first_ad_peoples) + second_ad_count > best_people:
                best_people = len(first_ad_peoples) + second_ad_count
                first_ad = cur_event[0]
                second_ad = second_event[0]
            # если уходит человек - уменьшаем счетчик second_ad_count
            if second_event[1] == 1 and second_event[2] not in first_ad_peoples:
                second_ad_count -= 1
        # когда человек ушел, убираем его из множества first_ad_peoples
        if cur_event[1] == 1:
            first_ad_peoples.remove(cur_event[2])

    # ответ
    print(best_people, first_ad, second_ad)
