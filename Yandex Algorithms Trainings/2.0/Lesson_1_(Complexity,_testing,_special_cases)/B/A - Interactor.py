# считываем данные
r = int(input().strip())  # код завершения задачи
i = int(input().strip())  # вердикт интерактора
c = int(input().strip())  # вердикт чекера

answer = -1  # переменная ответа
# ветвление в соответствии с условиями задачи
if i == 0:
    if r != 0:
        answer = 3
    else:
        answer = c
elif i == 1:
    answer = c
elif i == 4:
    if r != 0:
        answer = 3
    else:
        answer = 4
elif i == 6:
    answer = 0
elif i == 7:
    answer = 1
else:
    answer = i

# ответ
print(answer)