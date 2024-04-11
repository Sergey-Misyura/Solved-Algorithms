# считываем данные
n = int(input().strip())  # количество ягод
answer = [0] * n  # массив ответа
berries = [''] * (n + 1)  # массив значений ягод (поднимется за день, разница движения)

pos_diff_sum = 0  # кумулятивная сумма положительных разниц движений
for i in range(1, n + 1):  # заполняем berries
    a, b = map(int, input().split())
    diff = a - b
    berries[i] = (a, diff)
    pos_diff_sum += diff if diff > 0 else 0

# находим ягоду "достижения" макс высоты
idx_max = - 1  # индекс ягоды макс высоты
max_h = float('-inf')  # максимальная высота подъема
for i in range(1, n + 1):  # проходим по ягодам
    if berries[i][1] <= 0:  # если разница движений не положительная
        if pos_diff_sum + berries[i][0] > max_h:  # и если удалось увеличить высоту прибавлением "подъема" ягоды
            idx_max = i  # обновляем индекс макс высоты
            max_h = pos_diff_sum + berries[i][0]  # обновляем макс высоту
    else:  # иначе, если разница движений положительная
        # вычитаем из суммы положительных разниц прибавленную ранее разницу подъема/спуска ягоды, прибавляем 'подъем' ягоды
        if pos_diff_sum - berries[i][1] + berries[i][0] > max_h:  # и если удалось увеличить высоту
            idx_max = i  # обновляем индекс макс высоты
            max_h = pos_diff_sum - berries[i][1] + berries[i][0]  # обновляем макс высоту

# скармливаем улитке ягоды с положительной разницей и не idx_max
idx_answer = 0  # индекс в ответе
for i in range(1, n + 1):
    if berries[i][1] > 0 and i != idx_max:
        answer[idx_answer] = i
        idx_answer += 1
# скармливаем улитке 'максимальную' ягоду
answer[idx_answer] = idx_max
idx_answer += 1
# скармливаем улитке оставшиеся ягоды
for i in range(1, n + 1):
    if berries[i][1] <= 0 and i != idx_max:
        answer[idx_answer] = i
        idx_answer += 1

# ответ
print(max_h)
print(*answer)