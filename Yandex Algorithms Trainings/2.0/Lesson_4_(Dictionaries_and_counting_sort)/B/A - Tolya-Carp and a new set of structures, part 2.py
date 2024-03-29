from collections import defaultdict

# считываем данные
n = int(input().strip())  # количество посылок
sums = defaultdict(int)  # счетчик сумм цветов
for _ in range(n):
    # каждую посылку добавляем в счетчик
    color, num = map(int, input().split())
    sums[color] += num

answer = []  # массив ответа
# сохраняем каждый элемент счетчика sums в ответ
for key in sorted(sums.keys()):
    answer.append(str(key) + ' ' + str(sums[key]))

# ответ
print(*answer, sep='\n')