from collections import defaultdict

elections = defaultdict(int)  # счетчик голосов кандидатов
# считываем файл
with open('input.txt') as f:
    # из каждой строки заносим данные в счетчик
    for line in f.readlines():
        candidate, voices = line.split()
        elections[candidate] += int(voices)

answer = []  # массив ответа
# сохраняем каждый элемент счетчика elections в ответ
for key in sorted(elections.keys()):
    answer.append(key + ' ' + str(elections[key]))

# ответ
print(*answer, sep='\n')