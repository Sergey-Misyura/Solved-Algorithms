# считываем данные
N = int(input().strip())  # число касс
events = []  # массив открытий и закрытий касс
for i in range(N):
    a, b, c, d = map(int, input().split())
    # если время работы кассы не проходит через полночь, добавляем два события - открытие, закрытие кассы
    if c * 60 + d > a * 60 + b:
        events.append((a * 60 + b, 1))
        events.append((c * 60 + d, -1))
    # иначе разбиваем время работы кассы на два промежутка: до полуночи и после
    # закрытие кассы - флаг - 1, сначала касса закрывается, потом открывается
    else:
        events.append((a * 60 + b, 1))
        events.append((1440, -1))
        events.append((0, 1))
        events.append((c * 60 + d, -1))

# сортировка массива событий
events.sort()

answer = 0  # ответ
cur_count = 0  # текущее количество открытых касс
# проходим по массиву событий
for i in range(len(events)):
    # если при текущем событии все кассы открыты, добавляем разницу времени между текущим событием и предыдыущим
    # так как при N открытых касс текущее событие будет закрытие кассы, а предыдущее открытие кассы, что привело к N
    if cur_count == N:
        answer += events[i][0] - events[i - 1][0]
    # изменяем счетчик на тип события
    cur_count += events[i][1]

# ответ
print(answer)
