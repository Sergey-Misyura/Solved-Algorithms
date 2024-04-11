# считываем данные
N = int(input().strip())  # количество точек
dots = [0] * N  # массив точек

for i in range(N):  # записываем точки в массив
    x, y = map(int, input().split())
    dots[i] = (x, y)

dots_set = set(dots)  # множество точек
# создаем начальные значения ответа по первой точке, используя и вращая вектор (1,1), всего 3 добавляемые
second_dot = dots[0][0] + 1, dots[0][1] + 1
third_dot = dots[0][0] - 1, dots[0][1] + 1
fourth_dot = second_dot[0] - 1, second_dot[1] + 1
answer = [second_dot, third_dot, fourth_dot]  # ответ, минимальное количество добавляемых точек

for i in range(N - 1):  # проходим по первой точке в dots
    for j in range(i, N):  # проходим по второй точке в dots
        if dots[i] != dots[j]:  # если точки не накладываются
            vec1_x, vec1_y = dots[j][0] - dots[i][0], dots[j][1] - dots[i][1]  # считаем вектор от 1 ко 2 точке
            vec2_x, vec2_y = dots[i][0] - dots[j][0], dots[i][1] - dots[j][1]  # считаем вектор в обратном направлении от 2 к 1 точке

            need_1 = []  # необходимые точки по одну сторону от вектора, для составления первого квадрата
            point1 = (dots[i][0] - vec1_y, dots[i][1] + vec1_x)  # считаем первую необходимую точку от точки dots[i] с повернутым вектором 1
            point2 = (dots[j][0] + vec2_y, dots[j][1] - vec2_x)  # считаем вторую необходимую точку от точки dots[j] с повернутым вектором 2
            if point1 not in dots_set:  # проверяем наличие точки point1 в множестве dots_set, добавляем в need_1 если ее нет
                need_1.append(point1)
            if point2 not in dots_set:  # проверяем наличие точки point2 в множестве dots_set, добавляем в need_1 если ее нет
                need_1.append(point2)

            need_2 = []  # необходимые точки по другую сторону от вектора, для составления второго квадрата
            point3 = (dots[i][0] + vec1_y, dots[i][1] - vec1_x)  # считаем первую необходимую точку от точки dots[i] с другим поворотом вектора 1
            point4 = (dots[j][0] - vec2_y, dots[j][1] + vec2_x)  # считаем вторую необходимую точку от точки dots[j] с другим поворотом вектора 2
            if point3 not in dots_set:  # проверяем наличие точки point3 в множестве dots_set, добавляем в need_2 если ее нет
                need_2.append(point3)
            if point4 not in dots_set:  # проверяем наличие точки point4 в множестве dots_set, добавляем в need_2 если ее нет
                need_2.append(point4)
            # обновлем ответ - минимум точек из текущего ответа и двух вариантов расположения квадрата на векторе dots[i], dots[j]
            answer = min(answer, need_1, need_2, key=len)

# ответ
if len(answer) == 0:  # при найденных всех точках
    print(0)
else:  # если точки нужно добавить
    print(len(answer))
    print(*[str(x) + ' ' + str(y) for x, y in sorted(answer)], sep='\n')