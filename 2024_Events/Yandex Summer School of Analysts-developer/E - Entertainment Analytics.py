from math import pi

# считываем данные
L = float(input().strip())  # размер палки
N = float(input().strip())  # размер плитки

# ответ формула получаемая из "Задача Бюффона о бросании иглы" перестроенная для:
# 1. Квадратной плитки - вместо обычного r - r**2 (у нас N**2)
# 2. Вместо 2l вариантов получается l**2 вариантов, так как центр палки должна находится в 1 из 4 углов, в области между окружностью радиуса L и самим углом,
# поворот от 0 до pi/4 в каждом углу
print(L**2 / pi / N**2)