import sys
sys.setrecursionlimit(100000)


def all_ancestors(child, tree):
    """
    Функция сбора всех предков
    :param child: исходный потомок
    :param tree: генеалогическоe древо
    :return: множество предков
    """
    ancestors = set()  # множество предков
    while child in tree.keys():  # проходим от детей к родителям
        ancestors.add(child)  # добавляем в множество предков
        child = tree[child]
    ancestors.add(child)  # добавляем последнего предка
    return ancestors


def lca(child, potential_ancestors):
    """
    Функция поиска наименьшего общего предка
    :param child: ребенок
    :param potential_ancestors: множество потенциальных предков
    :return: наименьший общий предок
    """
    # проходим по предкам child пока не нашли общего предка или не пришли к корневому
    while child not in potential_ancestors and child in tree:
        child = tree[child]
    # если нашли предка из potential_ancestors возвращаем его
    if child in potential_ancestors:
        return child
    else:  # иначе предок - корень
        return ''


# считываем данные
with open('input.txt', 'r') as f:
    N = int(f.readline().strip())  # число элементов в генеалогическом древе
    tree = dict()  # генеалогическоe древо ребенок:[родитель]
    answer = []  # массив ответа
    # добавляем записи в генеалогическоe древо, кроме родоначальника
    for _ in range(N - 1):
        child, parent = f.readline().split()
        tree[child] = parent
    # проходим по данным для поиска самого раннего общего предка
    for line in f.readlines():
        human1, human2 = line.strip().split()  # человек 1 и человек 2
        ancestors = all_ancestors(human1, tree)  # предки человека 1
        answer.append(lca(human2, ancestors))  # добавляем в ответ общего предка
# ответ
print(*answer, sep='\n')
