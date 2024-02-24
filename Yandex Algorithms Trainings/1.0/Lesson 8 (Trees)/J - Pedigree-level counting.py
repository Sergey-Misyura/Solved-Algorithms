import sys
from collections import defaultdict

# считываем данные
N = int(input().strip())  # число элементов в генеалогическом древе
sys.setrecursionlimit(100000)
tree = defaultdict()  # генеалогическоe древо ребенок:[родитель]
people = set()  # множество людей в генеалогическом древe
heights_desc = defaultdict(int)  # счетчик числа уровней каждого человека

# добавляем запись в генеалогическоe древо, кроме родоначальника
for _ in range(N - 1):
    child, parent = input().split()
    people.add(child)
    people.add(parent)
    tree[child] = parent

def height_of_descendant(human):
    """
    Функция подсчета высоты элемента древа
    :param human: текущий человек
    :return: высоту в древе текущего элемента
    """
    # если человека нет в генеалогическом древе как потомка, сохраняем в heights_desc высоту 0, возвращаем 0
    if human not in tree:
        heights_desc[human] = 0
        return 0
    total_height = 0  # общая высота текущего элемента
    parent = tree[human]  # единственный родитель текущего человека
    # если высота родителя еще не подсчитана, рекурсивно вызываем height_of_descendant(parent)
    # сохраняем результат в счетчик heights_desc
    if parent not in heights_desc:
        height = height_of_descendant(parent)
        heights_desc[parent] = height
    # иначе получаем значение из счетчика heights_desc
    else:
        height = heights_desc[parent]
    # total_height - высота родителя плюс 1 уровень самого текущего человека
    total_height = height + 1
    # добавляем результат в счетчик heights_desc
    heights_desc[human] = total_height
    return total_height

# подсчет числа высот каждого человека, изменяет счетчик heights_desc
for human in people:
    height_of_descendant(human)

# вывод отсортированных по людям высот
for key in sorted(heights_desc.keys()):
    print(key, heights_desc[key])
