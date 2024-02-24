import sys
from collections import defaultdict

# считываем данные
N = int(input().strip())  # число элементов в генеалогическом древе
sys.setrecursionlimit(100000)
tree = defaultdict(list)  # генеалогическоe древо родитель:[дети]
people = set()  # множество людей в генеалогическом древe
count_desc = defaultdict(int)  # счетчик числа потомков каждого человека

# добавляем запись в генеалогическоe древо, кроме родоначальника
for _ in range(N - 1):
    child, parent = input().split()
    people.add(child)
    people.add(parent)
    tree[parent].append(child)

def count_of_descendants(human):
    """
    Функция подсчета количества потомков
    :param human: текущий человек
    :return: количество потомков текущего человека
    """
    # если человека нет в генеалогическом древе как родителя, возвращаем 0 потомков
    if tree[human] == []:
        return 0
    total_count = 0  # общее число потомков
    # проходим по детям в древе
    for child in tree[human]:
        # если для ребенка еще не посчитано число потомков, рекурсивно вызываем count_of_descendants() и
        # сохраняем ответ в счетчик count_desc
        if child not in count_desc:
            child_count = count_of_descendants(child)
            count_desc[child] = child_count
        # иначе получаем значение из счетчика
        else:
            child_count = count_desc[child]
        # увеличиваем total_count для текущего человека на число потомков child и самого child
        total_count += child_count + 1
    # добавляем полученный total_count в счетчик count_desc
    count_desc[human] = total_count
    return total_count

# подсчет количества потомков, изменяет счетчик count_desc
for human in people:
    count_of_descendants(human)

# вывод отсортированного числа потомков каждого человека
for key in sorted(count_desc.keys()):
    print(key, count_desc[key])
