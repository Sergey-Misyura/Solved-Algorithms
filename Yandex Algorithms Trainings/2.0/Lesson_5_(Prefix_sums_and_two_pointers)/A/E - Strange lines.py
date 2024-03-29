def rle(s):
    """
    Функция преобразования строки в rle массив
    :param s: входящая строка
    :return: rle - массив: буква, количество подряд
    """
    ans = [['#', 0]]
    for c in s:
        if ans[-1][0] == c:
            ans[-1][1] += 1
        else:
            ans.append([c, 1])
    return ans[1:]


s = input().strip()  # исходная строка
rle_s = rle(s)  # rle строка
singles = {}  # словарь подстрок из одиночных символов в rle строке
answer = 0  # ответ
for now in rle_s:  # проходим по символам в rle_s
    if now[0] not in singles:  # если еще не было символа - добавляем в словарь с длиной 0
        singles[now[0]] = 0
    prev_val = singles[now[0]]  # достаем из словаря предыдущую длину подстроки
    singles[now[0]] = max(singles[now[0]], now[1])  # обновляем в словаре максимальную длину продстроки
    answer += singles[now[0]] - prev_val  # добавляем в ответ разницу между текущей max и предыдущей max длиной
# странной подстрой будет являеться подстрока либо из одинаковых символов, либо вида - подряд идущие одни символы + подряд идущие вторые
pairs = {}  # словарь подстрок из пар символов в rle строке
for i in range(len(rle_s) - 1):  # проходим по символам в rle_s
    pair = rle_s[i][0], rle_s[i + 1][0]  # сохраняем пару
    if pair not in pairs:  # если пары еще не было - пустой список в pairs
        pairs[pair] = []
    pairs[pair].append((rle_s[i][1], rle_s[i + 1][1]))  # для пары, добавляем кортеж длин пары в pairs
for pair in pairs:  # проходим по парам в pairs
    f_len = {}  # словарь длин полей, образованных длинами из пар букв
    for now_len in pairs[pair]:  # проходим по списку длин в pairs[pair]
        # каждую уникальную первую длину в now_len сохраняем в f_len с максимальным возможным значением второй длины для нее
        if now_len[0] not in f_len:  # если не было - добавляем нулевую длину
            f_len[now_len[0]] = 0
        f_len[now_len[0]] = max(now_len[1], f_len[now_len[0]])  # обновляем первую длину максимальной вторйо для нее
    max_second = 0  # максимальная вторая длина
    # проходим по первым длинам - от большего к меньшему
    for now_first in sorted(f_len.keys(), reverse=True):
        now_max_second = max(max_second, f_len[now_first])  # обновляем текущую максимальную вторую длину
        # увеличиваем answer как при добавлении площади в графике XY (Х -первая длина, Y - вторая)
        answer += (now_max_second - max_second) * (now_first)  # добавленная площадь равна: изменению второй длины * первую длину
        max_second = now_max_second  # обновляем максимальную вторая длину

# ответ
print(answer)