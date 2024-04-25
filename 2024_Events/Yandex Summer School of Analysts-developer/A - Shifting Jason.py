import json

# считываем данные
json_name = input().strip()
with open(json_name, 'r') as f:
    trans = json.load(f)  # словарь преобразований
seqs = []  # массив строк вводимых фраз
for _ in range(len(trans)):
    seqs.append(input().split('_'))

output = dict()  # выходной словарь
for key, value in trans.items():  # проходим по словарю преобразований
    out_seq = []  # массив преобразованной строки фраз
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}  # гласные
    if value == '10':  # если код операции '10'
        for phrase in seqs[int(key) - 1]:  # проходим по фразам
            if len(set([c for c in phrase if c in vowels])) >= 2:  # если количество гласных не меньше 2 - добавляем в out_seq
                out_seq.append(phrase)
        output[key] = sorted(out_seq, reverse=True)  # сортируем out_seq и записываем в ответ
    elif value == '20':  # если код операции '20'
        out_seq = filter(lambda x: len(x) % 2 == 0, seqs[int(key) - 1])  # выбираем фразы с четной длиной
        output[key] = sorted(out_seq, reverse=True)  # сортируем out_seq и записываем в ответ
    else:  # иначе, если код операции '30'
        output[key] = sorted(seqs[int(key) - 1], reverse=True)  # сортируем строку фраз из seqs и записываем в ответ
# преобразуем output для вывода
with open('output.json', 'w') as f:
    json.dump(output, f, indent=4)