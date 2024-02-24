# считываем данные
N = int(input().strip())
shirts = list(map(int, input().split()))
M = int(input().strip())
pants = list(map(int, input().split()))

# текущие индексы в массивах shirts, pants
cur_shirt, cur_pant = 0, 0
# значения индексов при мин разнице
min_shirt, min_pant = 0, 0
# минимальная и текущая разница цветов
min_diff = cur_diff = float('inf')

# пока не вышли за пределы одного из массивов
while cur_shirt < N and cur_pant < M:
    # подсчет текущей разницы
    cur_diff = shirts[cur_shirt] - pants[cur_pant]
    # если текущая разница меньше минимальной разницы, сохраняем индексы
    if abs(cur_diff) < min_diff:
        min_shirt = cur_shirt
        min_pant = cur_pant
        min_diff = abs(cur_diff)

    # двигаем один из указателей в зависимости от знака cur_diff, так как оба массива возрастающие
    if cur_diff > 0:
        cur_pant += 1
    else:
        cur_shirt += 1

# ответ
print(shirts[min_shirt], pants[min_pant])


