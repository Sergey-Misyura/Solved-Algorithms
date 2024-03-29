# считываем данные
n, m = map(int, input().split())  # число вершин, число ребер в графе
vertex_set = set()  # множество ребер графа
# проходим по ребрам
for _ in range(m):
    v1, v2 = map(int, input().split())
    # если ребро не петля, добавляем в vertex_set как множество, убираем кратные ребра
    if v1 != v2:
        vertex_set.add(frozenset([v1, v2]))
# ответ
print(n, len(vertex_set))
# выводим ребра полученного графа
print(*[' '.join([str(a) for a in vertex]) for vertex in vertex_set], sep='\n')