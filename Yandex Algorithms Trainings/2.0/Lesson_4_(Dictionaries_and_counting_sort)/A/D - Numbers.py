from collections import Counter
# считываем данные
number1 = input().strip()  # первое число
number2 = input().strip()  # второе число
count1 = Counter(number1)  # счетчик символов первого числа
count2 = Counter(number2)  # счетчик символов второго числа

general_digit = dict()  # счетчик общих символов двух чисел
# проходим по счетчику первого числа и сравнивая с счетчиком второго числа добавляем общие символы в general_digit
for key, value in count1.items():
    if key in count2:
        general_digit[key] = min(count1[key], count2[key])

# ответ
# частный случай - если счетчик общих чисел пуст - выводим -1
if not general_digit:
    print(-1)
# иначе
else:
    # частный случай - если счетчик состоит только из 0 - выводим 0
    if len(general_digit.keys()) == 1 and '0' in general_digit.keys():
        print(0)
    # выводим строку состоящую из чисел счетчика по value раз в отсортированном по убыванию general_digit.items счетчике
    else:
        print(''.join([key*value for key, value in sorted(general_digit.items(), reverse=True)]))