# считываем данные
nums = set(list(map(int, input().split())))  # множество отображаемых кнопок
s = input().strip()
s_set = set()  # множество добавляемых кнопок

# добавляем кнопку в множество
for num in s:
    s_set.add(int(num))

diff = s_set - nums  # недостающие кнопки кнопки

# ответ
print(len(diff))


