from collections import deque

def bfs(graph, v):  # функция поиска в ширину
    distances = [(-1, -1) for _ in range(len(graph))]  # массив расстояний до вершины i вида: (предыдущая вершина на пути, расстояние до исходной)
    queue = deque()  # очередь
    distances[v] = (v, 0)  # расстояние начальной вершины
    queue.append(v)
    while queue:  # пока есть очередь
        cur_v = queue.popleft()  # берем из очереди вершину
        for next_v in graph[cur_v]:  # для каждого ее соседа
            if distances[next_v][1] == -1:  # если еще не обходили
                queue.append(next_v)  # добавляем в очередь
                distances[next_v] = (cur_v, distances[cur_v][1] + 1)  # сохраняем предыдущую вершину и расстояние до исходной
    return distances

# считываем данные
N = int(input().strip())  # число вершин
graph = [[] for _ in range(N)]  # граф
for _ in range(N - 1):  # добавляем вершины в граф
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


distances = bfs(graph, 0)  # находим начальные расстояния
first_max = max(range(len(distances)), key=lambda i: distances[i][1])  # выбираем самую дальнюю виршину
distances = bfs(graph, first_max)  # находим расстояния от уже выбранной вершины
second_max = max(range(len(distances)), key=lambda i: distances[i][1])  # находим вторую вершину самого длинного пути
# расстоянием ответа - расстояние от вершин на середине самого длинного пути
answer_dist = (distances[second_max][1] + distances[second_max][1] % 2) // 2
answer = []  # массив ответа
while second_max != first_max:  # восстанавливаем путь между полученными first_max и second_max вершинами
    answer.append(second_max)
    second_max = distances[second_max][0]
answer.append(first_max)

# ответ
if len(answer) % 2 == 0:  # если число вершин на пути четно - выводим расстояние ответа, число вершин 2, две средние вершины
    print(answer_dist, 2, answer[len(answer) // 2 - 1] + 1, answer[len(answer) // 2] + 1)
else:  # если число вершин четно - выводим расстояние ответа, число вершин 1, среднюю вершину
    print(answer_dist, 1, answer[len(answer) // 2] + 1)