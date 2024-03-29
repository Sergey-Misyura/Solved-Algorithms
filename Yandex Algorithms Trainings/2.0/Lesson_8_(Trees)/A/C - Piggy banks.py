# считываем данные
n = int(input().strip())
keys = [0] * (n + 1)  # массив расположения ключей в копилках
for i in range(1, n + 1):
    keys[i] = int(input())

mark = [0] * (n + 1)  # массив меток для копилок
answer = 0  # ответ
for i in range(1, n + 1):  # проходим по копилкам
    if mark[i] == 0:  # если копилка не помечена, помечаем ее номером
        now_piggy = i
        while mark[now_piggy] == 0:  # пока копилка не помечена
            mark[now_piggy] = i  # помечаем ее
            now_piggy = keys[now_piggy]  # переходим к копилке, в которой находится от нее ключ
        if mark[now_piggy] == i:  # если пришли к уже помеченной темже номером, разбивает ее
            answer += 1

# ответ
print(answer)