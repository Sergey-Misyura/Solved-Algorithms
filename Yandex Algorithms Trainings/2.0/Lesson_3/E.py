# считываем данные
m = int(input().strip())  # количество свидетелей
wits = [0] * m  # массив множеств свидетелей
for i in range(m):
    wits[i] = set(input().strip())
n = int(input().strip())  # количество номеров
nums = [0] * n  # массив номеров и сколько свидетелей видело
max_wit_count = 0  # максимальное число видевших свидетелей
# проходим по номерам
for i in range(n):
    num = input().strip()  # номер машины
    num_set = set(num)  # множество символов номера
    wit_count = 0  # число видевших свидетелей
    # проходим по свидетелям
    for wit in wits:
        # если множество символов номера включает множество символов свидетеля - увеличиваем счетчик wit_count
        if wit <= num_set:
            wit_count += 1
    # сохраняем в nums номер и число видевших свидетелей
    nums[i] = [num, wit_count]
    # обновляем max_wit_count
    max_wit_count = max(max_wit_count, wit_count)

# ответ
answer = []  # массив ответа
# проходим по nums и собираем в answer все номера с max_wit_count
for num, wit_count in nums:
    if wit_count == max_wit_count:
        answer.append(num)
# выводим ответ
print(*answer, sep='\n')