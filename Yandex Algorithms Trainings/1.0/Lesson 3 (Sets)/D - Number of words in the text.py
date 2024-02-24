# считываем данные
s = set()  # множество слов
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        # обновляем множество слов из строки
        s.update(set(line.split()))

# печатаем длину множества слов
print(len(s))
