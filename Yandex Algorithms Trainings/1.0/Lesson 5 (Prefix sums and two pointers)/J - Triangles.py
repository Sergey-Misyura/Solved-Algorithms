# считываем данные
n = int(input().strip())  # число точек
vertices = [] * n  # координаты точек
for _ in range(n):
    x, y = map(int, input().split())
    vertices.append((x, y))

answer = 0  # ответ

# проходим по вершинам
for i in range(n):
    # множество просмотренных векторов
    used_vectors = set()
    # соседи текущей вершины
    neighbors = []
    # проходим по соседям вершины
    for j in range(n):
        # считаем координты вектора
        vec_x = vertices[i][0] - vertices[j][0]
        vec_y = vertices[i][1] - vertices[j][1]
        # считаем квадрат длины стороны
        square_side_len = vec_x**2 + vec_y**2
        # добавляем квадрат длины в массив neighbors
        neighbors.append(square_side_len)
        # если есть вектор образующий прямую с текущим, то
        # вычитаем 1 из answer - лишний посчитанный треугольник, вырожденный в линию
        if (-vec_x, -vec_y) in used_vectors:
            answer -= 1
        # добавляем вектор в used_vectors
        used_vectors.add((vec_x, vec_y))

    # сортируем соседей по длине
    neighbors.sort()
    rg = 0  # правая граница раздвижного окна
    # проходим левым указателем раздвижного окна по соседям
    for lf in range(len(neighbors)):
        # двигаем правый указатель до первого отличающегося соседа
        while rg < len(neighbors) and neighbors[lf] == neighbors[rg]:
            rg += 1
        # добавляем в ответ количество посчитанных равнобедренных треугольников, для текущего окна
        answer += rg - lf - 1

# ответ
print(answer)