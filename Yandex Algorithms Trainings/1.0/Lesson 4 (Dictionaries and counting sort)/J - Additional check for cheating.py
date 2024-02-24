from collections import Counter

def clear_code(code):
    """
    функция "чистки" кода: убирает лишнее и возвращает код из чисел, букв и '_'
    :param code: входящий текст программы
    :return: 'очищенный' текст программы
    """
    ans = []
    for c in code:
        if c.isalpha() or c.isdigit() or c == '_':
            ans.append(c)
        else:
            ans.append(' ')
    return ''.join(ans)


def is_correct(word, start_digit):
    """
    функция проверки слова на корректность
    :param word: воходящее слово
    :param start_digit: может ли начинаться с цифры
    :return: True если корректно, иначе False
    """
    if word.isdigit():
        return False
    if not word[0].isdigit() or start_digit:
        return True
    return False


def main():
    with open('input.txt') as f:
        # считывание данных
        n, case_sens, start_digit = f.readline().strip().split()
        n = int(n)  # n - число ключевых слов
        # замена yes, no на bool
        case_sens = case_sens == 'yes'  # case_sens - регистр
        start_digit = start_digit == 'yes'  # start_digit - может начинаться с цифры

        # создаем словарь ключевых слов и добавляем их
        keywords = set()
        for _ in range(n):
            keyword = f.readline().strip()
            if not case_sens:
                keyword = keyword.lower()
            keywords.add(keyword)

        # создаем счетчик корректных идентификаторов
        word_counter = Counter()

        # считываем текст программы
        code = f.read()
        # чистим текст программы от лишних символов
        code = clear_code(code.strip())
        # подсчитываем идентификаторы
        for i, word in enumerate(code.split()):
            # если слово не чувствительно к регистру - переводим в нижний регистр
            if not case_sens:
                word = word.lower()
            # если слова нет в ключевых словах, а также оно корректно-для этого идентификатора увеличиваем word_counter
            if word not in keywords:
                if is_correct(word, start_digit):
                    word_counter[word] += 1
    # ответ - самый часто встречаемый идентификатор
    print(word_counter.most_common(1)[0][0])


if __name__ == '__main__':
    main()
