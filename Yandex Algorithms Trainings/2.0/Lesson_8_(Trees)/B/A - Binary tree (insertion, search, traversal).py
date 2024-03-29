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

    def search(self, num):
        """
        Функция поиска элемента в BST
        :return: bool найден или нет элемент
        """
        def _search(node, num):
            """
            Инкапсулированная рекурсивная функция поиска элемента в BST
            :param node: текущий узел
            :param num: искомое значение
            :return: pass
            """
            # если значение узла больше искомого числа - уходим влево
            if node.val > num:
                # если слева нет узла - выводим NO
                if node.left is None:
                    print('NO')
                # иначе влево рекурсивно вызываем _search
                else:
                    _search(node.left, num)
            # иначе, если значение узла меньше искомого числа - уходим вправо
            elif node.val < num:
                # если справа нет узла - выводим NO
                if node.right is None:
                    print('NO')
                # иначе вправо рекурсивно вызываем _search
                else:
                    _search(node.right, num)
            else:  # если нашли - выводим YES
                print('YES')

        # при пустом корне - выводим NO
        if self.root is None:
            print('NO')
        else:
            _search(self.root, num)

    def add(self, num):
        """
        Функция добавления узла в BST
        :param num: добавляемое значение
        :return: выводит "DONE" или "AlREADY"
        """
        def _add(node, num):
            """
            Инкапсулированная рекурсивная функция добавления узла в BST
            :param node: текущий узел
            :param num: добавляемое значение
            :return: выводит "DONE" или "AlREADY"
            """
            # если значение узла больше добавляемого числа - уходим влево
            if node.val > num:
                # если слева нет узла - создаем узел с добавляемым числом, выводим DONE
                if node.left is None:
                    node.left = Node(num)
                    print('DONE')
                # иначе влево рекурсивно вызываем _add
                else:
                    _add(node.left, num)
            # иначе, если значение узла меньше добавляемого числа - уходим вправо
            elif node.val < num:
                # если справа нет узла - создаем узел с добавляемым числом, выводим DONE
                if node.right is None:
                    node.right = Node(num)
                    print('DONE')
                # иначе вправо рекурсивно вызываем _add
                else:
                    _add(node.right, num)
            else:  # выводим ALREADY
                print('ALREADY')
        # при пустом корне создаем узел с добавляемым значением, выводим DONE
        if self.root is None:
            self.root = Node(num)
            print('DONE')
        else:
            _add(self.root, num)

    def printtree(self):
        """
        Функция распечатывания BST
        :return: выводит BST в виде дерева
        """

        def _print_node_on_level(node, depth=0):
            """
            Инкапсулированная рекурсиваная функция распечатывания узла на каждом уровне BST
            :param node: текущий узел
            :param depth: глубина
            :return: вид узла на каждом уровне BST
            """
            if not node:  # если нет узла - ничего не возвращаем
                return

            if node.left:  # если есть узел слева - идем налево
                _print_node_on_level(node.left, depth + 1)
            print(f"{''.join('.' * depth)}{node.val}")  # распечатываем текущий узел на соответствующем ему уровне
            if node.right:  # если есть узел справа - идем направо
                _print_node_on_level(node.right, depth + 1)

        _print_node_on_level(self.root, depth=0)

# создаем экземпляр дерева
tree = BST()

# считываем данные
with open('input.txt', 'r') as f:
    for line in f.readlines():
        command = list(line.split())  # команда для дерева
        if len(command) == 2:  # если команда ADD или SEARCH
            command[1] = int(command[1])
            if command[0] == 'ADD':
                tree.add(command[1])
            else:
                tree.search(command[1])
        else:  # иначе, если команда PRINTTREE
            tree.printtree()
