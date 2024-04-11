import sys

#sys.set_int_max_str_digits(1000000)  # настройка для контеста
n, K, D = map(int, input().split())  # изначальная прибыль, количество учредителей компании и количество дней, которое вы собираетесь следить за прибылью
# находим первую цифру для подстановки в конец значения прибыли
n *= 10  # заранее добавим 0 в конец прибыли
next_digit = -1  # новое цифра
for i in range(10):  # проходим по цифрам
    if next_digit == -1:  # если не нашли цифру
        # проверяем делимость новой прибыли при дописывании цифры в конец старой прибыли
        if (n + i) % K == 0:  # если поделили - сохраняем найденную цифру
            next_digit = i

if next_digit == -1:  # если не нашли первую добавляемую цифру - ответ -1
    print(-1)
else:
    answer = [''] * D  # массив ответа
    answer[0] = str(n + next_digit)  # сохраняем str значение начальной прибыли + дописанная найденная цифра
    if D > 1:  # если можем двигаться по массиву далее
        for i in range(1, D):  # проходим по массиву
            answer[i] = '0'  # добавляем 0, каждый раз увеличивая найденное число в 10 раз
    # выводим ответ
    print(''.join(answer))
