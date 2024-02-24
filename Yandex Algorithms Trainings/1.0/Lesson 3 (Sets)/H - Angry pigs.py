# считываем данные
N = int(input().strip())

coords_set = set()  # множество координат Х

# сохраняем координаты Х во множество координат
for _ in range(N):
    x, _ = map(int, input().split())
    coords_set.add(x)

# ответ - длина множества
print(len(coords_set))