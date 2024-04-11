from collections import Counter

# считываем данные
count_1 = Counter(input().strip())  # счетчик слова 1
count_2 = Counter(input().strip())  # счетчик слова 2
# ответ
if count_1 == count_2:  # если счетчики совпадают
    print('YES')
else:
    print('NO')