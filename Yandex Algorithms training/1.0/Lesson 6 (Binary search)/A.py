# считываем данные
N, K = map(int, input().split())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

answer = []
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

    if arr_1[lf] == arr_2[i]:
        answer.append('YES')
    else:
        answer.append('NO')

# ответ
print('\n'.join(answer))
