from collections import deque
import sys

sys.setrecursionlimit(100000)

def dfs(graph, v, visited, subtree_size, depth):
    """
    Функция обхода в глубину
    :param graph: граф городов
    :param v: текущая вершина
    :param visited: массив посещенных городов
    :param subtree_size: массив размеров поддерева
    :param depth: массив глубин узлов
    :return: возвращает размер поддерева в v, обновляет subtree_size, depth
    """
    visited[v] = True  # отметка о посещенности города
    subtree_size[v] += 1  # увеличение поддерева на сам v
    for u in graph[v]:  # проходим по соседям v
        if not visited[u]:  # если город еще не посещен
            depth[u] = depth[v] + 1  # изменяем глубину u
            subtree_size[v] += dfs(graph, u, visited, subtree_size, depth)  # увеличиваем subtree_size[v], запуская dfs
    # возвращаем размер поддерева в v
    return subtree_size[v]

def main():
    n = int(input())  # количество городов
    graph = [[] for _ in range(n)]  # граф
    for _ in range(n - 1):  # заполняем граф
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n  # массив посещенных городов
    subtree_size = [0] * n  # массив размеров поддерева
    depth = [0] * n  # массив глубин узлов
    dfs(graph, 0, visited, subtree_size, depth)  # запускаем обход в глубину на графе для заполнения subtree_size, depth
    s = 0   # текущая суммарная удаленность
    for i in range(n):  # проходим по depth для подсчета суммарной удаленности в корне
        s += depth[i]
        visited[i] = False
    res = [0] * n  # массив сумаарных удаленностей
    res[0] = s  # обновляем корневое значение
    st = deque()  # стек проверяемых вершин
    st.append(0)  # добавляем корень в стек
    # проходим по дереву, считаем суммарные удаленности для res
    while st:  # пока есть стек
        v = st.pop()  # достаем вершину
        visited[v] = True  # ставим пометку о посещенности
        for u in graph[v]:  # для каждого связанного с v города
            if not visited[u]:  # если город не посещен
                res[u] = res[v] + n - 2 * subtree_size[u]  # считаем res[u] как res[v] + изменение расстояния при сдвиге из v в u
                st.append(u)  # добавляем город u в стек
    tmp = [(res[i], i) for i in range(n)]  # формируем список сумм удаленности с индексом
    tmp.sort()  # сортируем
    res_idx = []  # массив индексов ответа
    res_idx.append(tmp[0][1])  # добавляем индекс первого города в список
    for i in range(1, n):  # добавляем остальные города с такой же суммарной удаленностью
        if tmp[i][0] == tmp[0][0]:
            res_idx.append(tmp[i][1])
        else:
            break

    # ответ
    print(tmp[0][0], len(res_idx), end=" ")  # минимальная суммарная удаленность
    for idx in res_idx:
        print(idx + 1, end=" ")  # список городов
    print()

if __name__ == "__main__":
    main()
