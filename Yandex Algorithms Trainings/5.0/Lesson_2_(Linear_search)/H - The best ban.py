# считываем данные
n, m = map(int, input().split())  # количество рас и классов
max_in_row = [0] * n * 2  # массив максимум строк
# смысл задачи - вычеркивание максимумов по строке и столбцу, для проведения линии достаточно двух точек,
# поэтому повзьмем по два максимума в каждой строке
for i in range(n):
    cur_race = list(map(int, input().split()))
    max_1, idx_max_1, max_2, idx_max_2 = -1, -1, -1, -1  # первый максимум, его индекс, второй максимум, его индекс
    for j in range(m):  # находим первый и второй максимум строки
        if max_1 <= cur_race[j]:
            max_2 = max_1
            idx_max_2 = idx_max_1
            max_1 = cur_race[j]
            idx_max_1 = j
        elif max_2 < cur_race[j]:
            max_2 = cur_race[j]
            idx_max_2 = j

    max_in_row[i*2] = (max_1, i, idx_max_1)  # сохраняем первый максимум, его строку, его индекс
    max_in_row[i*2+1] = (max_2, i, idx_max_2)  # сохраняем второй максимум, его строку, его индекс

max_in_row.sort(key=lambda x: -x[0])  # сортируем массив только по убыванию значения, остальное по возрастанию

answer_row, answer_col = -1, -1  # переменные ответа
if max_in_row[0][1] != max_in_row[1][1] and max_in_row[0][2] != max_in_row[1][2]:  # если первые два числа max_in_row не совпадают ни по одной оси, проверяем третье число
    if max_in_row[2][1] == max_in_row[0][1]:  # при совпадении строки 3 числа и 1
        answer_row, answer_col = max_in_row[0][1], max_in_row[1][2]  # строка чисел 3 и 1, столбец 2 числа
    elif max_in_row[2][2] == max_in_row[0][2]:  # при совпадении столбца 3 числа и 1
        answer_row, answer_col = max_in_row[1][1], max_in_row[0][2]  # строка 2 числа, столбец чисел 3 и 1
    elif max_in_row[2][1] == max_in_row[1][1]:  # при совпадении строки 3 числа и 2
        answer_row, answer_col = max_in_row[1][1], max_in_row[0][2]  # строка чисел 3 и 2, столбец 1 числа
    elif max_in_row[2][2] == max_in_row[1][2]:  # при совпадении столбца 3 числа и 2
        answer_row, answer_col = max_in_row[0][1], max_in_row[1][2]  # строка 1 числа, столбец чисел 3 и 2
    else:  # если третье число не совпадает не совпадает по осям ни с первым, ни со вторым - выбираем из первого и второго любые оси
        answer_row, answer_col = max_in_row[0][1], max_in_row[1][2]
elif max_in_row[0][1] == max_in_row[1][1]:  # в случае если у 1 и 2 чисел совпадает строка, тогда у 3 берем столбец
    answer_row = max_in_row[0][1]
    answer_col = max_in_row[2][2]
elif max_in_row[0][2] == max_in_row[1][2]:  # в случае если у 1 и 2 чисел совпадает столбец, тогда
    answer_col = max_in_row[0][2]  # обновляем столбец ответа
    cur_idx = 2  # текущий индекс в max_in_row
    while answer_col == max_in_row[cur_idx][2]:  # проходим по оставшимся числам max_in_row, пока не найдем столбец отличный от answer_col
        cur_idx += 1
    answer_row = max_in_row[cur_idx][1]  # обновляем строку ответа
# ответ
print(answer_row + 1, answer_col + 1)