from collections import Counter
# считываем данные
N, M = map(int, input().split())  # число строк квадратной головоломки, число ключевых слов
table_sym_count = Counter()  # счетчик всех букв в головоломке
# проходим по строкам головоломки
for _ in range(N):
    row = input().strip()
    # добавляем к счетчику всех символов table_sym_count счетчик символов строки
    table_sym_count.update(Counter(row))

# проходим по строкам
for _ in range(M):
    word = input().strip()
    # вычитаем из счетчика всех символов table_sym_count счетчик символов слова
    table_sym_count.subtract(Counter(word))

# ответ - выводим строку для символов оставшихся в table_sym_count, умножая ключ на количество повторений - значение
print(''.join([key*value for key, value in table_sym_count.items() if value > 0]))