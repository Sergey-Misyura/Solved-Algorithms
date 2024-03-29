from collections import Counter

_ = input()  # число символов в строке
seq = input().strip()  # входящая строка символов
sym_count = Counter(seq)  # счетчик символов в seq
mid_sym = ''  # средний символ палиндрома
left_part = []  # массив левой стороны палиндрома

# проходим па отсортированным символам в счетчике sym_count
for key, value in sorted(sym_count.items()):
    repeats, rem = divmod(value, 2)  # число повторений в левой части палиндрома, указатель четности количества символов
    # если средний символ палиндрома не заполнен и количество повторений символа нечетное - добавляем символ в середину
    if mid_sym == '' and rem == 1:
        mid_sym = key
    # добавляем сивол к левой стороне палиндрома repeats раз
    for _ in range(repeats):
        left_part.append(key)

# ответ
# если есть только центральный символ - выводим mid_sym
if not left_part:
    print(mid_sym)
# иначе конкатенируем строку полученную из left_part с mid_sym, и со строкой из отраженной left_part
else:
    print(''.join(left_part) + mid_sym + ''.join(left_part[::-1]))