# считываем данные
N = int(input().strip())

turtle_set = set()  # множество ответов
truth_count = 0  # счетчик правдивых ответов
for _ in range(N):
    before, after = map(int, input().split())  # идет до, идет после
    # если текущего ответа еще не было и сумма равна числу оставшихся черепах
    if (before, after) not in turtle_set and before + after == N - 1:
        # если оба числа не отрицательны, увеличиваем счетчик ответов, добавляем ответ в множество
        if before >= 0 and after >= 0:
            truth_count += 1
            turtle_set.add((before, after))

# печатаем количество правдивых ответов
print(truth_count)



