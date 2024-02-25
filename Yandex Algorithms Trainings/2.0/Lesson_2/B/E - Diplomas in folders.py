# считываем данные
folders = int(input().strip())  # количество папок
diploms = list(map(int, input().split()))  # массив дипломов в папках
diploms.sort()  # сортируем массив
# ответ - время на просмотр всех папок, кроме самой большой
print(sum(diploms[:-1]))