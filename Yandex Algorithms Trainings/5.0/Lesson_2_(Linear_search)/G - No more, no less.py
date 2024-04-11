# считываем данные
t = int(input().strip())  # число тестов

for _ in range(t):  # для каждого теста
    n = int(input().strip())
    seq = list(map(int, input().split()))  # последовательнеость

    answer = []  # массив ответа
    cur_min, cur_count = float('inf'), 0  # текущий минимум, текущее количество чисел на отрезке
    for i in range(n):  # проходим по числам
        if seq[i] >= cur_count + 1 and cur_min >= cur_count + 1:  # если добавляемое число не меньше новой длины отрезка и минимум на новом отрезке не меньше длины
            cur_min = min(cur_min, seq[i])  # пересчитываем минимум
            cur_count += 1  # увеличиваем длину отрезка чисел
        else:  # иначе делаем разрез
            answer.append(cur_count)  # добавляем длину отрезка к ответу
            cur_min = seq[i]  # обновляем минимум отрезка
            cur_count = 1  # обновляем длину отрезка
    # добавляем последний отрезок к ответу
    answer.append(cur_count)
    # ответ
    print(len(answer))
    print(*answer)