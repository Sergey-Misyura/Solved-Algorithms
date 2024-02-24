from collections import defaultdict

def main():
    # считываем данные
    N = int(input().strip())

    dct = defaultdict(list)  # словарь слов и список индексов его ударения
    for _ in range(N):
        word = input().strip()

        # добавляем слово в нижнем регистре и индекс его ударения
        for i in range(len(word)):
            if word[i].isupper():
                dct[word.lower()].append(i)

    seq = input().split()  # проверяемый текст
    all_errors = 0  # общее число ошибок в тексте

    # проходим по слову в тексте
    for word in seq:

        n_upper = -1  # индекс ударения в текущем слове, -1 указывает что ранее в слове не встречалось ударение
        error = False  # флаг ошибки в слове
        # проходим по буква в слове
        for i in range(len(word)):
            # когда находим ударение
            if word[i].isupper():
                # если ударения еще не было, сохраняем индекс ударения
                if n_upper == -1:
                    n_upper = i
                # иначе флаг ошибки в слове True, завершаем проход по слову
                else:
                    error = True
                    break
        # если была ошибка в слове или мы не нашли ударения - увеличиваем общее число ошибок в тексте
        if error or n_upper == -1:
            all_errors += 1
        # иначе, если ошибок в слове не было, проверяем слово по словарю
        else:
            word_lower = word.lower()
            # если слово в словаре, а в списке ударений нет найденного ударения в слове n_upper - общее число ошибок +1
            if word_lower in dct.keys():
                if n_upper not in dct[word_lower]:
                    all_errors += 1

    # ответ
    print(all_errors)


if __name__ == '__main__':
    main()
