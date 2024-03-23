from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def bfs(vert, tree):
    """
    Функция Breadth first search
    :param vert: начало обхода
    :param tree: дерево обхода
    :return: массив расстояний в бусинках от начала
    """
    visited = [0] * (N + 1)  # массив флагов посещенных вершин
    distances = [-1] * (N + 1)  # массив расстояний
    distances[vert] = 0  # расстояние начальной от начальной
    visited[vert] = 1  # флаг в начальную вершину
    queue = [vert]  # очередь для текущего уровня bfs
    cur_dist = 0  # текущая дистанция
    while queue:  # пока еще есть уровни дерева
        cur_dist += 1  # увеличиваем дистанцию
        second_queue = []  # очередь следующего уровня обхода
        for cur_vert in queue:  # проходим по каждой вершине в очереди
            for next_vert in tree[cur_vert]:  # проходим по следующим вершинам от текущей
                if visited[next_vert] == 0:  # если вершина не посещена
                    distances[next_vert] = cur_dist  # записываем расстояние
                    second_queue.append(next_vert)  # добавляем в очередь следующего уровня
                    visited[next_vert] = 1  # ставим флаг visited
        queue = second_queue  # переходим на следующий уровень bfs
    # возвращаем массив расстояний в бусниках
    return distances


# считываем данные
N = int(input().strip())  # количество бусинок
tree = defaultdict(list)  # дерево
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

distances = bfs(1, tree)  # 1 проход bfs - считаем расстояние в бусинках от любой бусинки до остальных
farther_vert = distances.index(max(distances))  # находим самую дальнюю бусинку
sec_distances = bfs(farther_vert,
                    tree)  # 2 проход bfs - считаем расстояние в бусинках от найденной бусинки до остальных
tree_diameter = max(sec_distances) + 1  # количество = максимальное расстояние + 1 одна бусинка
# ответ
print(tree_diameter)
