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
        Функция подсчета высоты BST
        :return: высоту
        """
        def _traverse(node):
            """
            Инкапсулированная рекурсивная функция обхода BST для подсчета высоты
            :param node: текущий узел
            :return: высоту от текущего узла
            """
            # если пустой узел - возвращаем 0
            if node is None:
                return 0
            # рекурсия влево
            left_height = _traverse(node.left)
            # рекурсия вправо
            right_height = _traverse(node.right)
            # вовзвращаем высоту поддеревьев + 1, высоту узла
            return max(left_height, right_height) + 1

        return _traverse(self.root)

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
            # если значение узла больше добавляемого числа - уходим влево
            if node.val > num:
                # если слева нет узла - создаем узел с добавляемым числом
                if node.left is None:
                    node.left = Node(num)
                # иначе влево рекурсивно вызываем _add
                else:
                    _add(node.left, num)
            # иначе, если значение узла меньше добавляемого числа - уходим вправо
            elif node.val < num:
                # если справа нет узла - создаем узел с добавляемым числом
                if node.right is None:
                    node.right = Node(num)
                # иначе вправо рекурсивно вызываем _add
                else:
                    _add(node.right, num)
        # при пустом корне создаем узел с добавляемым значением
        if self.root is None:
            self.root = Node(num)
        else:
            _add(self.root, num)

# создаем экземпляр дерева
tree = BST()

# считываем данные
nums = list(map(int, input().split()))
# добавляем узлы в дерево и считаем высоту
for num in nums:
    if num == 0:
        print(tree.height())
    else:
        tree.add(num)
