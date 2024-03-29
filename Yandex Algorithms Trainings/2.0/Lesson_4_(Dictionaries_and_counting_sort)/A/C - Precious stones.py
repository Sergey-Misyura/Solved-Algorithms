from collections import defaultdict
# считываем данные
n, k = map(int, input().split())  # число камней, которые привезли купцы и число пар, которые шах считает красивыми
beautiful_pairs = defaultdict(list)  # словарь списков пар - второй камень пары: [первые камни пары]
stones_count = defaultdict(int)  # счетчик количества камней в ряду

stones_row = input().strip()  # ряд камней
# добавляем пары в словарь списков пар
for _ in range(k):
    pair = input().strip()
    beautiful_pairs[pair[1]].append(pair[0])

total_pairs_count = 0  # итоговое число найденных красивых пар
# проходим по камням в ряду
for stone in stones_row:
    # далее проходим по первым камням пары текущего камня
    for previous_stone in beautiful_pairs[stone]:
        # если уже был встречен такой камень - увеличиваем итог на количество встреченных ранее первых камней
        if previous_stone in stones_count:
            total_pairs_count += stones_count[previous_stone]

    # увеличиваем счетчик текущего камня в stones_count
    stones_count[stone] += 1

# выводим ответ
print(total_pairs_count)