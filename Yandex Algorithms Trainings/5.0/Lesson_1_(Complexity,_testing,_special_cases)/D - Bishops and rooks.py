def figure_walks(row, col, grid, shifts):  # функция движения фигуры
    for shift in shifts:  # для каждого смещения
        cur_row, cur_col = row + shift[0], col + shift[1]  # устанавливаем текущие строку и столбец
        # пока не вышли за границу доски и не встретили фигуру
        while -1 < cur_row < 8 and -1 < cur_col < 8 and grid[cur_row][cur_col] != 'R' and grid[cur_row][cur_col] != 'B':
            # если встретили пустую клетку, заменяем на битую клетку
            grid[cur_row][cur_col] = '#' if grid[cur_row][cur_col] == '*' else grid[cur_row][cur_col]
            # переходим к следующей клетке
            cur_row += shift[0]
            cur_col += shift[1]


# считываем данные
grid = []  # массив доски
for _ in range(8):
    row = list(input().strip())
    grid.append(row)

rook_shifts = ((-1, 0), (0, 1), (1, 0), (0, -1))  # смещения ладьи
elephant_shifts = ((-1, 1), (1, 1), (1, -1), (-1, -1))  # смещения слона
# проходим по доске
for row in range(8):
    for col in range(8):
        if grid[row][col] == 'R':  # если нашли ладью - запускаем функцию движения фигуры с rook_shifts
            figure_walks(row, col, grid, rook_shifts)
        elif grid[row][col] == 'B':  # иначе если нашли слона - запускаем функцию движения фигуры с elephant_shifts
            figure_walks(row, col, grid, elephant_shifts)

empty_cells = 0  # количество пустых небитых клеток
for row in range(8):  # проходим по доске, при пустой небитой клетке увеличиваем счетчик
    for col in range(8):
        empty_cells += 1 if grid[row][col] == '*' else 0
# ответ
print(empty_cells)