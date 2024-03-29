from collections import Counter
# считываем данные
name1 = input().strip()  # первое имя
name2 = input().strip()  # второе имя

count_name1 = Counter(name1)  # счетчик символов в имени1
count_name2 = Counter(name2)  # счетчик символов в имени2
intersect = count_name1.keys() & count_name2.keys()  # общие буквы в именах
answer = []  # массив ответа
# продолжаем пока есть общие буквы
while len(intersect) > 0:
    max_sym = max(intersect)  # лексикографически максимальная буква из общих
    used_max_sym = min(count_name1[max_sym], count_name2[max_sym])  # число повторений буквы в обоих именах
    answer.append(max_sym * used_max_sym)  # добавляем в ответ букву * число ее повторений
    name1 = name1.replace(max_sym, '#', used_max_sym)  # заменяем использованные буквы в имени1 на #
    name1 = name1[name1.rfind('#') + 1:]  # находим букву после последней # и убираем всю предыдущую часть имени1
    name2 = name2.replace(max_sym, '*', used_max_sym)  # заменяем использованные буквы в имени2 на *
    name2 = name2[name2.rfind('*') + 1:]  # находим букву после последней * и убираем всю предыдущую часть имени2
    count_name1 = Counter(name1)  # пересчитываем буквы в имени1
    count_name2 = Counter(name2)  # пересчитываем буквы в имени2
    intersect = count_name1.keys() & count_name2.keys()  # пересчитываем общие буквы в именах

# ответ
print(''.join(answer))