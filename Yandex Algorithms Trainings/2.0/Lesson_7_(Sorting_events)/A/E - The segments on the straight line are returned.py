# считываем данные
n = int(input().strip())  # число отрезков
events = []  # массив событий отрезков
for i in range(n):
    start, end = map(int, input().split())
    events.append((end, end - start, start, i))  # добавляем отрезок кортежем вида: (конец, длина, начало, номер)
events.sort()  # сортируем события

answer = [0] * n  # массив ответа
prev_segments = []  # стек еще невложенных отрезков
for cur_end, cur_len, cur_start, cur_num in events:  # проходим по массиву событий
    while len(prev_segments) > 0 and cur_start <= prev_segments[-1][0]:  # пока в стеке отрезки помещаются в текущий
        _, prev_num = prev_segments.pop()  # достаем отрезок из стека
        answer[prev_num] = cur_num + 1  # для полученного отрезка записываем текущий cur_num, покрывающий его
    prev_segments.append((cur_start, cur_num))  # добавляем текущий отрезок в стек
# ответ
print(*answer)