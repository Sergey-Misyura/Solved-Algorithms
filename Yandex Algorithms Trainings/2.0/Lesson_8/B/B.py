import sys
sys.setrecursionlimit(100000)


def search_parent(child, target, tree):
    """
    Функция поиска предка в дереве
    :param child: ребенок
    :param target: искомый предок
    :param tree: генеалогическое древо
    :return: bool Найден ли искомый предок
    """
    is_parent = False  # флаг найденного target предка
    while not is_parent and child in tree.keys():  # пока предок не найден и ребенок есть в дереве
        if tree[child] == target:  # если родитель ребенка соответствует target - флаг True
            is_parent = True
        else:  # иначе переходим к родителю ребенка
            child = tree[child]
    # возвращаем флаг
    return is_parent


# считываем данные
with open('input.txt', 'r') as f:
    N = int(f.readline().strip())  # число элементов в генеалогическом древе

    tree = dict()  # генеалогическоe древо ребенок:[родитель]
    answer = []  # массив ответа
    # добавляем записи в генеалогическоe древо, кроме родоначальника
    for _ in range(N - 1):
        child, parent = f.readline().split()
        tree[child] = parent
    # проходим по данным для поиска элементам
    for line in f.readlines():
        human1, human2 = line.strip().split()  # человек 1 и человек 2
        parent_1_2 = search_parent(human2, human1, tree)  # функция поиска предка
        parent_2_1 = search_parent(human1, human2, tree)  # функция поиска предка
        if parent_1_2:  # если 1 человек - предок 2 - в ответ 1
            answer.append(1)
        elif parent_2_1:  # если 2 человек - предок 1 - в ответ 2
            answer.append(2)
        else:  # иначе в ответ 0
            answer.append(0)
# ответ
print(*answer)
