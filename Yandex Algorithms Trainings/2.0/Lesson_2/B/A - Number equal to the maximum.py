from collections import Counter
# считываем данные
nums_count = Counter()  # счетчик повторений чисел
cur_num = int(input().strip())  # текущее число
nums_count[cur_num] += 1  # увеличиваем счетчик
max_num, max_count = cur_num, 1   # максимальное число, количество его повторений

# пока не дошли до 0
while cur_num != 0:
    cur_num = int(input().strip())
    nums_count[cur_num] += 1  # увеличиваем счетчик
    # если пришло максимальное число - обновляем max_num, max_count
    if cur_num >= max_num:
        max_count = nums_count[cur_num]
        max_num = cur_num

# ответ
print(max_count)