def binSearchLeft(lf, rg, check, checkparams, min_height):  # функция левого бинпоиска, возвращает найденную мин высоту и число схождения
    while lf < rg:
        mid = (lf + rg) // 2
        part2_biggest, next_height = check(mid, checkparams)  # вторая часть больше первой, полученная высота
        min_height = min(min_height, next_height)  # обновляем мин высоту рулона
        # усредняем высоты частей, двигаясь каждый раз к меньшей
        if part2_biggest:  # если вторая часть больше первой, сужаем первую часть, двигаем rg на mid
            rg = mid
        else:  # иначе, если первая часть не меньше второй, сужаем вторую часть
            lf = mid + 1
    # возвращаем мин высоту рулона и левую границу схождения
    return min_height, lf


def check_height(m, checkparams):  # функция проверки высоты рулона, возвращает больше ли вторая высота чем первая, и макс высоту
    part1, part2, w = checkparams  # часть1, часть2, ширина
    height1, height2 = height_calc(m, part1), height_calc(w - m, part2)  # полученные высоты частей рулона

    return height2 > height1, max(height1, height2)


def height_calc(width, words):  # функция расчета высоты части рулона при width ширине
    height = 1  # начальная высота
    rem = width  # свободное место в строке
    for word in words:  # проходим по словам
        if rem != width:  # если не в начале строки, добавляем пробел к слову
            word += 1
        if word < rem:  # если места больше чем нужно, записываем слово, уменьшаем rem
            rem -= word
        elif word == rem:  # если место ровно сколько надо - записываем слово, увеличиваем высоту
            height += 1
            rem = width
        else:  # иначе, если места не хватает, добавляем строку, в нее пишем слово
            height += 1
            rem = width - word + 1

    if rem == width:  # если в конце пустая строка, после word == rem, убираем ее
        height -= 1
    # возвращем высоту части рулона при width ширине
    return height

# считываем данные
w, n, m = map(int, input().split())  # ширина рулона, количество слов в первой и второй части рапорта
part1 = list(map(int, input().split()))  # массив слов первой части
part2 = list(map(int, input().split()))  # масси в слов второй части
max_len1 = max(part1)  # длина первой части
max_len2 = max(part2)  # длина второй части
start_height = max(height_calc(max_len1, part1), height_calc(max_len2, part2))  # начальная высота бин поиска
# левый бин посик по ответу
answer, bound = binSearchLeft(max_len1, w - max_len2, check_height, (part1, part2, w), start_height)  # ответ. граница разделения
# дополнительная проверка ответа и границы разделения, после выхода из бин поиска, если сошлись бин поиском и внутри не заходили в цикл проверки
answer = min(answer, max(height_calc(bound, part1), height_calc(w - bound, part2)))

# ответ
print(answer)
