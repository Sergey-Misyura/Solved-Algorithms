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

    def height(self):
        """
        Функция подсчета высты BST
        :return: высоту
        """

        def _height_traverse(node):
            """
            Инкапсулированная рекурсивная функция обхода BST для подсчета высоты
            :param node: текущий узел
            :return: высоту от текущего узла
            """
            if node is None:
                return 0
            left_height = _height_traverse(node.left)
            right_height = _height_traverse(node.right)
            return max(left_height, right_height) + 1

        return _height_traverse(self.root)

    def add(self, num):
        """
        Функция добавления узла в BST
        :param num: добавляемое значение
        :return: pass
        """

        def _add(node, num):
            """
            Инкапсулированная рекурсивная функция добавления узла в BST
            :param node: текущий узел
            :param num: добавляемое значение
            :return: pass
            """
            if node.val > num:
                if node.left is None:
                    node.left = Node(num)
                else:
                    _add(node.left, num)
            elif node.val < num:
                if node.right is None:
                    node.right = Node(num)
                else:
                    _add(node.right, num)

        if self.root is None:
            self.root = Node(num)
        else:
            _add(self.root, num)

    def second_max(self):
        """
        Функция поиска второго максимума BST
        :return: второй максимум BST
        """
        def _second_max_traverse(node, prev_val, go_left):
            """
            Инкапсулированная рекурсивная функция обхода BST для поиска второго максимума
            :param node: текущий узел
            :param prev_val: значение узла родителя
            :param go_left: флаг поворота налево (второй максимум хранится или у родителя максимума дерева, либо у левого потомка максимума)
            :return: возвращает значение узла (второй максимум)
            """
            # если есть узел справа - рекурсивно вызываем _second_max_traverse в нем
            if not (node.right is None):
                return _second_max_traverse(node.right, node.val, go_left)
            # иначе, если есть узел слева и налево еще не ходили - рекурсивно вызываем _second_max_traverse в левом узле
            elif not (node.left is None) and not go_left:
                return _second_max_traverse(node.left, node.val, True)
            # возвращаем значение текущего узла если ходили налево, иначе значение узла родителя
            return node.val if go_left else prev_val

        return _second_max_traverse(self.root, None, False)
# создаем экземпляр дерева
tree = BST()

# считываем данные
nums = list(map(int, input().split()))
# добавляем узлы в дерево
for num in nums:
    if num != 0:
        tree.add(num)
# выводим второй максимум
print(tree.second_max())
