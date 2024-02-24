# считываем данные
gen1 = input().strip()
gen2 = input().strip()

set_gen2 = set()  # множество пар оснований второго генома
# проходим по второму геному, добавляем пары
for i in range(1, len(gen2)):
    set_gen2.add(gen2[i-1:i+1])

count = 0  # степень близости генома
# проходим по второму геному, если пара есть во множестве второго - увеличиваем счетчик
for i in range(1, len(gen1)):
    if gen1[i-1:i+1] in set_gen2:
        count += 1

# ответ
print(count)



