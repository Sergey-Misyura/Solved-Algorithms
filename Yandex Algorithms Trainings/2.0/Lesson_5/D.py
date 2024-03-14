# считываем данные
seq = input().strip()  # скобочная последовательность
type = {'(': 1, ')': -1}  # массив номерных типов скобок
count_brackets = 0  # количество скобок
# проходим по seq
for bracket in seq:
    # изменяем счетчик count_brackets в зависимости от скобки
    count_brackets += type[bracket]
    # если закрыли скобок больше чем открыли - ответ NO, break
    if count_brackets < 0:
        print('NO')
        break
# если завершили цикл без прерывания
else:
    # проверяем count_brackets на оставшиеся открытые скобки, если есть - ответ NO, иначе YES
    if count_brackets != 0:
        print('NO')
    else:
        print('YES')