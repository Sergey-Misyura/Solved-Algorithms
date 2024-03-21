# считываем данные
N = int(input().strip())  # количество грузов
segments = [0] * (N*2)  # массив событий для грузов
for i in range(0, N*2, 2):
    start, time = map(int, input().split())
    # обновляем массив segments, сначала груз уходит -1, потом дугой приходит 1
    segments[i] = [start, 1]
    segments[i + 1] = [start + time, -1]
# сортируем массив
segments.sort()

div_count = 0  # число аппаратов
cur_div_count = 0  # текущее число аппратов
for event in segments:  # проходим по массиву событий
    cur_div_count += event[1]  # меняем текущее число автоматов
    if event[1] == 1:  # при прибытии груза обновляем div_count
        div_count = max(div_count, cur_div_count)
# ответ
print(div_count)
