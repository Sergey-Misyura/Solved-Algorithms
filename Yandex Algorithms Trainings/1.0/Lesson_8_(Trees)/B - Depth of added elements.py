class Node:
    """
    Класс Узел
    """
    def __init__(self, val=None, left=None, right=None):
        """
        Конструктор узла
        :param val: значение
        :param left: левый потомок
        :param right: правый потомок
        """
        self.val = val
        self.left = left
        self.right = right


class BST:
    """
    Класс -  Бинарное Дерево Поиска
    """
    def __init__(self):
        """
        Конуструктор BST. Создается пустой корень.
        """
        self.root = None


    def add(self, num):
        """
        Функция добавления узла в BST
        :param num: добавляемое значение
        :return: высота добавляемого значения
        """
        def _add(node, num):
            """
            Инкапсулированная рекурсивная функция добавления узла и счета высоты этого узла в BST
            :param node: текущий узел
            :param num: добавляемое значение
            :return: высота добавляемого значения по отношению к текущему узлу
            """
            # если текущий узел больше добавляемого - идем влево
            if node.val > num:
                # если узла нет - добавляем его, возвращаем высоту 1
                if node.left is None:
                    node.left = Node(num)
                    return 1
                # если такой узел есть и высота None - возвращаем None, иначе возвращаем полученную рекурсивно высоту + 1
                else:
                    height = _add(node.left, num)
                    return None if height is None else height + 1
            # если текущий узел меньше добавляемого - идем вправо
            elif node.val < num:
                # если узла нет - добавляем его, возвращаем высоту 1
                if node.right is None:
                    node.right = Node(num)
                    return 1
                # если такой узел есть и высота None - возвращаем None, иначе возвращаем полученную рекурсивно высоту + 1
                else:
                    height = _add(node.right, num)
                    return None if height is None else height + 1

        # если корень пуст - создаем узел, возвращаем высоту 1
        if self.root is None:
            self.root = Node(num)
            return 1
        # если получили None - значит число уже в дереве, возвращаем None, иначе выводим полученную рекурсивно высоту + 1
        else:
            height = _add(self.root, num)
            return None if height is None else height + 1

# создаем экземпляр дерева
tree = BST()

# считываем данные
nums = list(map(int, input().split()))
# добавляем узлы в дерево и выводим высоту каждого узла, если высота не None
for num in nums:
    if num != 0:
        height = tree.add(num)
        if height is not None:
            print(height, end=' ')
