# считываем данные
n = int(input().strip())  # число игроков
scores = list(map(int, input().split()))  # баллы игроков
nums = list(map(int, input().split()))  # массив загаданных чисел в последнем туре
used = set()  # множество загаданных чисел
used_twice = set()  # множество повторяющихся загаданных чисел
# добавляем числа в used и used_twice
for num in nums:
    if num in used:
        used_twice.add(num)
    used.add(num)

nums.append(0)  # добавляем последний ответ в массив загаданных чисел
best_losers = -1  # лучшее число проигравших Пете
best_num = -1  # лучшее последнее загаданное число
# проходим по массиву возможных вариантов последнего ответа
for added_num in range(1, 102):
    # копируем множества для изменений
    cur_scores = scores.copy()
    cur_used = used.copy()
    cur_used_twice = used_twice.copy()
    # изменяем последний ответ на added_num
    nums[-1] = added_num
    # если ответ уже был, добавляем во множество cur_used_twice
    if added_num in cur_used:
        cur_used_twice.add(added_num)
    cur_used.add(added_num)
    win = 102  # число - победитель игры
    # проходим по возможным вариантам ответа, обновляем число-победитель
    for cur in range(101, 0, -1):
        if cur in cur_used and cur not in cur_used_twice:
            win = cur
    # проходим по массиву cur_scores - начисляем очки победителю
    for i in range(len(cur_scores)):
        if nums[i] == win:
            cur_scores[i] += win
    cur_losers = 0  # текущее число игроков, проигравших Пете
    # проходим по массиву cur_scores - подсчитываем cur_losers
    for i in range(len(cur_scores) - 1):
        if cur_scores[i] < cur_scores[-1]:
            cur_losers += 1
    # если нашли большее значение проигравших - сохраняем его и лучшее для Пети число
    if cur_losers > best_losers:
        best_losers = cur_losers
        best_num = added_num

# ответ
print(best_num)




