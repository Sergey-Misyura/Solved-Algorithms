# считываем данные
seq = list(map(int, input().split()))  # последовательность чисел

answer = ['NO'] * len(seq)  # массив ответа
set_nums = set()  # множество чисел
# проходим по числам
for i in range(len(seq)):
    # если число не встречалось - добавляем в set_nums
    if seq[i] not in set_nums:
        set_nums.add(seq[i])
    # иначе меняем в массиве ответ на 'YES'
    else:
        answer[i] = 'YES'

# ответ
print(*answer, sep='\n')