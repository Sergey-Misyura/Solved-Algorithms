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
            :param go_left: флаг поворота налево (второй максимум хранится или у родителя максимума дерева, либо у левого потомка)
            :return: возвращает значение узла (второй максимум)
            """
            if not (node.right is None):
                return _second_max_traverse(node.right, node.val, go_left)
            elif not (node.left is None) and not go_left:
                return _second_max_traverse(node.left, node.val, True)
            return node.val if go_left else prev_val

        return _second_max_traverse(self.root, None, False)

    def traverse(self):
        """
        Функция обхода BST min - max
        :return:
        """
        def _traverse(node):
            """
            Инкапсулированная рекурсивная функция обхода BST (идем влево до упора, печатаем текущий узел, идем вправо на шаг)
            :param node: текущий узел
            :return: выводит узлы min - max
            """
            if not (node.left is None):
                _traverse(node.left)
            print(node.val)
            if not (node.right is None):
                _traverse(node.right)

        _traverse(self.root)

    def leaf_traverse(self):
        """
        Функция обхода листьев BST min - max
        :return:
        """
        def _leaf_traverse(node):
            """
            Инкапсулированная рекурсивная функция обхода листьев BST (идем влево до упора, печатаем текущий лист, идем вправо на шаг)
            :param node: текущий узел
            :return: выводит листы min - max
            """
            if not (node.left is None):
                _leaf_traverse(node.left)
            if node.right is None and node.left is None:
                print(node.val)
            if not (node.right is None):
                _leaf_traverse(node.right)

        _leaf_traverse(self.root)

    def fork_traverse(self):
        """
        Функция обхода развилок BST min - max
        :return:
        """
        def _fork_traverse(node):
            """
            Инкапсулированная рекурсивная функция обхода развилок BST (идем влево до упора, печатаем текущую развилку, идем вправо на шаг)
            :param node: текущий узел
            :return: выводит развилки min - max
            """
            if not (node.left is None):
                _fork_traverse(node.left)
            if not (node.left is None) and not (node.right is None):
                print(node.val)
            if not (node.right is None):
                _fork_traverse(node.right)

        _fork_traverse(self.root)

    def branch_traverse(self):
        """
        Функция обхода веток BST, узлов с одним ребенком, от min до max
        :return: выводит ветки до min до max
        """
        def _branch_traverse(node):
            """
            Инкапсулированная рекурсивная функция обхода веток BST (идем влево до упора, печатаем текущую ветку, идем вправо на шаг)
            :param node: текущий узел
            :return: выводит ветки до min до max
            """
            # если есть узел слева - идем до упора влево
            if not (node.left is None):
                _branch_traverse(node.left)
            # пройдя влево, если у узла только 1 ребенок - вывод значения узла
            if (not (node.left is None) and node.right is None) or (node.left is None and not (node.right is None)):
                print(node.val)
            # после вывода значения - делаем шаг вправо
            if not (node.right is None):
                _branch_traverse(node.right)

        # вывод веток до min до max
        _branch_traverse(self.root)


# создаем экземпляр BST
tree = BST()

# считываем данные
nums = list(map(int, input().split()))
# добавляем узлы в BST, пока не 0
for num in nums:
    if num != 0:
        tree.add(num)

# обход веток BST
tree.branch_traverse()
