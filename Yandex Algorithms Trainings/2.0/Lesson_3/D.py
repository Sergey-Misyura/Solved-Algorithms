# считываем данные
n = int(input().strip())  # n — наибольшее загадываем число
set_yes = set()  # множество чисел в котором есть загадываемое число
list_no = []  # массив чисел без загаданного числа

question = input().strip()  # текущий задаваемый вопрос
# пока вопрос не 'HELP'
while question != 'HELP':
    seq = list(map(int, question.split()))  # значит это список чисел
    result = input().strip()  # ответ на вопрос
    # если число есть в вопросе
    if result == 'YES':
        # и если множество YES пустое, заменяем пустое множество YES
        if len(set_yes) == 0:
            set_yes = set(seq)
        # иначе обновляем множество YES пересечением
        else:
            set_yes = set_yes & set(seq)
    # если ответ был NO
    else:
        # и если массив NO пустой, заменяем пустой массив NO
        if len(list_no) == 0:
            list_no = seq
        # иначе, увеличиваем массив NO
        else:
            list_no.extend(seq)

    question = input().strip()  # новый вопрос

# переводим массив NO во множество NO
set_no = set(list_no)
# если множество YES не пустое - ответ разница множеств YES и NO
if len(set_yes) > 0:
    print(*sorted(set_yes - set_no))
# иначе генерируем ответ, выкидывая числа, находящиеся в NO
else:
    print(*[i for i in range(1, n + 1) if i not in set_no])