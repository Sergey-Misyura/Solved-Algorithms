# считываем данные
N, K = map(int, input().split())  # N элементов массива 1, K элементов массива 2
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

answer = []  # массив ответов
# проходим по массиву 2
for i in range(K):
    # используем левый бин поиск
    lf, rg = 0, N - 1
    while lf < rg:
        # считаем центр
        mid = (lf + rg) // 2
        # если число больше чем в центре то сдвигаем левый указатель на mid + 1
        if arr_1[mid] < arr_2[i]:
            lf = mid + 1
        # если число меньше или равно числу в центре, сдвигаем правый указатель на mid
        else:
            rg = mid
    # результат бин поиска в arr_1[lf]

    # если сошлись на lf и он 0, или число на позиции lf ближе к искомому чем число на lf-1, добавляем в ответ arr_1[lf]
    if lf == 0 or abs(arr_2[i] - arr_1[lf]) < abs(arr_2[i] - arr_1[lf - 1]):
        answer.append(str(arr_1[lf]))
    # иначе ближайшее число arr_1[lf - 1]
    else:
        answer.append(str(arr_1[lf - 1]))

# ответ
print('\n'.join(answer))
