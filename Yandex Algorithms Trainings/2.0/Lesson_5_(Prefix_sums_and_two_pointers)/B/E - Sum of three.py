# считываем данные
S = int(input().strip())  # искомая сумма
arr_a = list(map(int, input().split()))[1:]  # массив чисел a
arr_b = list(map(int, input().split()))[1:]  # массив чисел b
arr_c = list(map(int, input().split()))[1:]  # массив чисел c

answer = []  # ответ
nums_c = dict()  # словарь чисел c и их индексов
# заполняем словарь c
for i in range(len(arr_c)):
    # добавляем запись если числа еще не было
    if arr_c[i] not in nums_c.keys():
        nums_c[arr_c[i]] = i

# проходим по a
for i in range(len(arr_a)):
    # если есть ответ, прерываем цикл
    if len(answer) != 0:
        break
    # проходим по b
    for j in range(len(arr_b)):
        c = S - arr_a[i] - arr_b[j]  # необходимое число в c
        # если c есть в nums_c, сохраняем ответ, break
        if c in nums_c.keys():
            answer.append((i, j, nums_c[c]))
            break

# ответ
if len(answer) == 0:
    print(-1)
else:
    print(*answer[0])
