N, x, y = map(int, input().split())
first_copier = min(x, y)
second_copier = max(x, y)

if N == 1:
    # время для печати 1 копии
    print(first_copier)
else:
    # время для печати всех кроме первой
    lf, rg = 0, first_copier * (N-1)
    # левый бин поиск
    while lf < rg:
        # считаем центр
        mid = (lf + rg) // 2
        # если не успели напечатать N - 1 копий - сдвигаем lf на mid + 1
        if mid // first_copier + mid // second_copier < N - 1:
            lf = mid + 1
        # иначе сдвигаем rg на mid
        else:
            rg = mid
    # ответ
    print(lf + first_copier)