def bodyswap(p1, p2):
    """
    Функция перемещения сознания между двумя персонами
    :param p1: первая персона
    :param p2: вторая персона
    :return: печатаем путь перемещения, возвращает значение сознания у второй персоны
    """
    print(p1, p2)
    persons[p1], persons[p2] = persons[p2], persons[p1]
    # сознание второй персоны
    return persons[p2]

# считываем данные
n, m = map(int, input().split())  # количество героев Футурамы и количество произведенных обменов разумами
persons = [i for i in range(n + 1)]  # массив сознаний героев, индексы - тела
# начальные переносы
for _ in range(m):
    p1, p2 = map(int, input().split())
    persons[p1], persons[p2] = persons[p2], persons[p1]

# проходим по массиву сознаний, не включая последних двух персон
for i in range(1, n - 1):
    # если у персоны отичное от нее сознание
    if persons[i] != i:
        cur = i  # текущая персона
        # пока не вернемся снова к текущей персоне
        while persons[cur] != i:
            # перемещаем сознание из текущей персоны, в n - 1 персону, сознание в n - 1 делаем текущей персоной
            cur = bodyswap(cur, n - 1)
        # из-за невозможности перемещат в n - 1 персону - перемещение сознаний в n персону, после перемещение из n - 1
        cur = bodyswap(cur, n)
        cur = bodyswap(cur, n)
        bodyswap(persons[n - 1], n - 1)
# проверка последних двух сознаний на правильность расположения
if persons[n - 1] == n:
    bodyswap(n - 1, n)


