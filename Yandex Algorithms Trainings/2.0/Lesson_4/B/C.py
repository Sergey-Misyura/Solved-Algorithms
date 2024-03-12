from collections import defaultdict

count = defaultdict(int)  # счетчик частот слов
# считываем данные
with open('input.txt') as f:
    # из каждой строки файла добавляем слова в счетчик
    for line in f.readlines():
        for word in line.split():
            count[word] += 1

count_list = list(count.items())  # массив слов с их частотами
# сортируем массив сначала по частоте, потом по лексикографическому порядку
count_list.sort(key=lambda x: [-x[1], x[0]])
# выводим в ответ отсортированные слова
print(*[word for word, count in count_list], sep='\n')
