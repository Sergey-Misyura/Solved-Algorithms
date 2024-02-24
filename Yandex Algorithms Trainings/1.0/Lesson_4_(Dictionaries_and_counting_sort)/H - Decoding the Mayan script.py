def main():
    # считываем данные
    g, s = map(int, input().split())  # количество знаков в слове, количество знаков в последовательности
    word = input().strip()  # искомое слово
    seq = input().strip()  # последовательность

    answer = 0  # переменная ответа
    # массив-счетчик букв, показывает на сколько далеко в текущем состоянии мы находимся от искомого слова
    word_counter = [0] * (123 - 65)  # длина основана на кодах символов в Unicode
    # добавляем каждую букву слова в word_counter
    for sym in word:
        word_counter[ord(sym) - 65] += 1

    matching_count = 0  # счетчик совпавших и несовпавших букв
    # частичный проход по seq, в длину g искомого слова для обновления matching_count
    for i in range(g):
        ord_sym = ord(seq[i]) - 65  # код символа уменьшенный на 65, используется для индекса в matching_count
        # подсчитываем совпадение букв
        # счетчик matching_count увеличиваем только если в в массиве-счетчике word_counter есть ранее посчитанная буква
        if word_counter[ord_sym] > 0:
            matching_count += 1
        # иначе уменьшаем matching_count
        else:
            matching_count -= 1
        # уменьшаем word_counter
        word_counter[ord_sym] -= 1

    # если число совпадений равно длине слова - увеличиваем ответ
    if matching_count == g:
        answer += 1

    # основной цикл прохода по seq, окном, i - правая граница
    for i in range(g, s):
        left_sym = ord(seq[i - g]) - 65  # индекс в word_counter левой границы окна
        # сначала изменяем word_counter и matching_count убирая left_sym окна
        if word_counter[left_sym] >= 0:
            matching_count -= 1
        else:
            matching_count += 1
        word_counter[left_sym] += 1

        cur_ord = ord(seq[i]) - 65  # индекс в word_counter правой границы окна
        # теперь изменяем word_counter и matching_count добавляя cur_ord, правый символ окна
        if word_counter[cur_ord] > 0:
            matching_count += 1
        else:
            matching_count -= 1
        word_counter[cur_ord] -= 1

        # если число совпадений равно длине слова - увеличиваем ответ
        if matching_count == g:
            answer += 1

    # ответ
    print(answer)


if __name__ == '__main__':
    main()
