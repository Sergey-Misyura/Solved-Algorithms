# считываем данные
N, M = map(int, input().split())  # N групп, M аудиторий
groups = [(group, i + 1) for i, group in enumerate((map(int, input().split())))]  # пронумерованные группы студентов
classes = [(cls, i + 1) for i, cls in enumerate((map(int, input().split())))]   # пронумерованные аудитории
groups_places = [0] * (N + 1)  # массив содержит номера аудиторий куда посадили i группу студентов

# сортируем массивы групп и студентов
groups.sort()
classes.sort()
cur_class, cur_group = 0, 0  # текущие указатели в массивах
# пока не вышли за границы массива
while cur_group < N and cur_class < M:
    # жадно выбираем аудиторию, если количество мест в ней больше количества студентов
    if classes[cur_class][0] > groups[cur_group][0]:
        # записываем аудиторию в groups_places
        groups_places[groups[cur_group][1]] = classes[cur_class][1]
        cur_group += 1  # сдвигаем указатель в группах
    cur_class += 1  # сдвигаем указатель в аудиториях

# ответ - число групп - указатель + 1 последней рассаженной группы
print(cur_group)
# выводим номера аудиторий
print(*groups_places[1:], sep='\n')
