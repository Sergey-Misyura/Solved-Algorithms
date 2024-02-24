# считываем данные
n = int(input().strip())

dct = dict()  # словарь синонимов

# заносим слова в словарь
for _ in range(n):
    a, b = input().split()
    dct[a] = b
    dct[b] = a

# ответ
print(dct[input()])