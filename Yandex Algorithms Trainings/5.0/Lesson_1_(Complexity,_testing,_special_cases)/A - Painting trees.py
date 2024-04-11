# считываем данные
P, V = map(int, input().split())  # координата краски, расстояние действия
Q, M = map(int, input().split())  # координата краски, расстояние действия
seg1 = [P - V, P + V]  # считаем отрезок 1 действия краски
seg2 = [Q - M, Q + M]  # считаем отрезок 2 действия краски
seg1, seg2 = sorted([seg1, seg2])  # сортируем отрезки
# ответ
if seg2[0] <= seg1[1]:  # если отрезки пересекаются - выводим итоговый отрезок + 1 дерево
    print(max(seg2[1], seg1[1]) - seg1[0] + 1)
else:  # иначе выводим сумму = длина отрезка + 1 дерево
    print(sum((seg1[1] - seg1[0] + 1, seg2[1] - seg2[0] + 1)))
