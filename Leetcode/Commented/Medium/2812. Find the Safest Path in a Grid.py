"""
2812. Find the Safest Path in a Grid
(Medium complexity)

You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

A cell containing a thief if grid[r][c] = 1
An empty cell if grid[r][c] = 0
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.
"""


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)  # размер поля
        queue, safeness = deque(), [[-1] * n for _ in range(n)]  # очередь, безопасное расстояние от клетки до "вора"
        unseen = set(product(range(n), range(n)))  # непросмотренные клетки
        neighbors = lambda x, y: set(((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1))) & unseen  # функция для получения соседних, непосещенных клеток

        for i, j in product(range(n), range(n)):  # проходим по полю
            if grid[i][j] == 1:  # если нашли вора
                safeness[i][j] = 0  # ставим в safeness 0
                queue.append((0, i, j))  # добавляем в очередь (safeness, i, j)
        while queue:  # пока есть еще 'воры'
            s, x, y = queue.popleft()  # получаем значение из очереди
            for cur_x, cur_y in neighbors(x, y):  # находим непосещенных соседей
                if safeness[cur_x][cur_y] == -1:  # если у соседа отсутствует safeness
                    safeness[cur_x][cur_y] = s + 1  # увеличиваем на 1
                    queue.append((s + 1, cur_x, cur_y))  # добавляем его в очередь (safeness, i, j)

        heap = [(-safeness[-1][-1], n - 1, n - 1)]  # heap с искомой клеткой
        while heap:  # пока есть heap
            s, x, y = heappop(heap)  # достаем клетку
            if (x, y) == (0, 0): return min(-s, safeness[0][0])  # когда пришли к началу - возвращаем мин safeness
            unseen.discard((x, y))  # убираем полученную клетку из непосещенных
            for cur_x, cur_y in neighbors(x, y):  # для каждого непосещенного соседа текущей клетки
                safe = max(s, -safeness[cur_x][cur_y])  # выбираем мин safeness
                heappush(heap, (safe, cur_x, cur_y))  # ложим его в heap
                unseen.discard((cur_x, cur_y))  # убираем из непосещенных
        # если пути нет ответ -1
        return -1