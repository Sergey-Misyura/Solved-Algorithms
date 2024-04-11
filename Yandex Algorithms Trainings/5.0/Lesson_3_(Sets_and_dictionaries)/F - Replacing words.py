# считываем данные
input_dict = list(input().split())  # массив заданного словаря
seq = list(input().split())  # массив слов

reduc_dict = dict()  # словарь сокращений вида - длина сокращения: множество сокращений этой длины
# заполняем словарь сокращений
for word in input_dict:
    if len(word) not in reduc_dict.keys():
        reduc_dict[len(word)] = {word}
    else:
        reduc_dict[len(word)].add(word)

for i in range(len(seq)):  # проходим по словам в seq
    for cur_len in range(len(seq[i])):  # проходим по длине сокращений каждого слова
        if cur_len + 1 in reduc_dict.keys():  # если длина сокращения есть в reduc_dict
            if seq[i][:cur_len + 1] in reduc_dict[cur_len + 1]:  # проверяем, есть ли само сокращение в reduc_dict
                seq[i] = seq[i][:cur_len + 1]  # сокращаем слово

# ответ
print(*seq)