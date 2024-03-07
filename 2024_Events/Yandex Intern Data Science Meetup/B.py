# OK
# считываем данные
N, S = map(int, input().split())  # количество заявок от туристов и вместимость приюта
tourists = []  # массив времени пребывания туристов
for _ in range(N):
    tourists.append(int(input().strip()))
tourists.sort()  # сортируем массив

if N <= S:  # если туристов не более чем мест - ответ INF
    print('INF')
else:
    timediff = float('inf')  # максимальное время проживания в отеле
    lf = 0  # левый указатель
    cur_count = 0  # текущее число туристов
    for rg in range(N):  # проходим правым указателем по массиву tourists
        cur_count += 1  # увеличиваем текущее число туристов
        if cur_count == S + 1:  # если превысили число проживающих
            timediff = min(timediff, tourists[rg] - tourists[lf])  # обновляем время проживания
            prev_tourist = tourists[lf]  # запоминаем время первого прибывшего на отрезке
            while tourists[lf] == prev_tourist and lf < rg:  # двигаем левый указатель до следующего време, уменьшаем cur_count
                lf += 1
                cur_count -= 1

    # ответ
    if timediff <= 0:  # если время проживания не целое положительное - ответ Impossible
        print('Impossible')
    else:  # иначе выводим максимальное время проживания
        print(timediff)