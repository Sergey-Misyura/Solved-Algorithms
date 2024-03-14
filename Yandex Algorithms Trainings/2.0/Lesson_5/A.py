# считываем данные
n, q = map(int, input().split())  # количество чисел, количество запросов
nums = list(map(int, input().split()))  # массив чисел
pref_sums = [0] * (n + 1)  # массив префиксных сумм
# считаем pref_sums
for i in range(0, n):
    pref_sums[i+1] = pref_sums[i] + nums[i]

answer = []  # переменная ответа
# добавляем в answer разницу между rg и lf из pref_sums по каждому запросу
for _ in range(q):
    lf, rg = map(int, input().split())
    answer.append(pref_sums[rg] - pref_sums[lf - 1])

# ответ
print(*answer, sep='\n')