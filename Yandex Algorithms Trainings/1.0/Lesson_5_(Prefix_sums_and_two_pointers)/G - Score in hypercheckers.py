from collections import Counter

# считываем данные
n, k = map(int, input().split())
cards = list(map(int, input().split()))

# подсчитываем количество одинаковых карт
count = Counter(cards)

# отсортированный массив уникальных карт
uniqnums = list(count.keys())
uniqnums.sort()

rg = 0  # правый указатель раздвижного окна
answer = 0  # ответ
duplicates = 0  # число дубликатов
# проходимся левой границей раздвижного окна по uniqnums
for lf in range(len(uniqnums)):
    # пока левое число меньше правого в не более k раз
    while rg < len(uniqnums) and uniqnums[lf] * k >= uniqnums[rg]:
        # подсчитываем дубликаты
        if count[uniqnums[rg]] >= 2:
            duplicates += 1
        rg += 1
    # длина текущего раздвижного окна
    window_len = rg - lf
    # добавляем 3 варианта ответа на каждое оставшееся число при счетчике lf карты >= 2
    if count[uniqnums[lf]] >= 2:
        answer += (window_len - 1) * 3
    # добавляем 1 вариант ответа при счетчике lf карты >= 3
    if count[uniqnums[lf]] >= 3:
        answer += 1
    # добавляем варианты ответа для прогрессии в текущем раздвижном окне, используя его длину
    answer += (window_len - 1) * (window_len - 2) * 3

    # убираем дубликаты, посчитанные ранее с uniqnums[lf]
    if count[uniqnums[lf]] >= 2:
        duplicates -= 1
    # добавляем в ответ варианты для дублируихся чисел, каждый дубликат дает 3 варианта
    answer += duplicates * 3

# ответ
print(answer)






