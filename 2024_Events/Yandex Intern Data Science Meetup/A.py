# 6 тест "Неверное решение"
from collections import defaultdict

# считываем данные
p, n, k = map(int, input().split())  # число видео, число отобранных, ограничение на 1 тему
themes = [''] * p  # массив тем
answer = [''] * n  # массив отобранных видео
for i in range(p):
    themes[i] = input().strip()

id_vid = list(map(int, input().split()))  # массив id видео
viewed_themes = set()  # множество уже просмотренных тем
count_vid = defaultdict(int)   # счетчик просмотренных тем
ans_i = 0  # индекс элемента в массиве ответа
for i in range(len(themes)):  # проходим по всем видео
    if ans_i == n:  # если заполнили ответ - завершаем
        break
    if themes[i] not in viewed_themes:  # если темы еще нет в просмотренных
        count_vid[themes[i]] += 1  # увеличиваем счетчик тем
        answer[ans_i] = str(themes[i]) + ' #' + str(id_vid[i])  # добавляем видео в ответ
        ans_i += 1  # увеличиваем индекс в ответе

        if count_vid[themes[i]] >= k:  # если занесли уже тему k раз - добавляем в просмотренные
            viewed_themes.add(themes[i])

# ответ
print(*answer, sep='\n')
