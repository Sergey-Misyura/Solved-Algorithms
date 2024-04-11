# считываем данные
K = int(input().strip())  # количество клеток
min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')  # координаты углов прямоугольника

for _ in range(K):
    x, y = map(int, input().split())
    min_x = min(min_x, x)  # находим минимальный х
    min_y = min(min_y, y)  # находим минимальный y
    max_x = max(max_x, x)  # находим максимальный x
    max_y = max(max_y, y)  # находим максимальный y
# ответ
print(min_x, min_y, max_x, max_y)