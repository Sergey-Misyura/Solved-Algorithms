# считываем данные
n = int(input().strip())  # количество чисел
nums = list(map(int, input().split()))  # массив чисел
pref_sums = [0] * (n + 1)  # массив префиксных сумм
max_sum = nums[0]  # максимальная сумма на отрезке
min_pref_sum = 0  # минимальная префиксная сумма

# проходим по числам
for i in range(0, n):
    pref_sums[i+1] = pref_sums[i] + nums[i]
    # максимальная сумма на отрезке - разность текущей преф суммы и мин преф суммы
    # обновляем максимальную сумму
    max_sum = max(max_sum, pref_sums[i + 1] - min_pref_sum)
    # обновляем минимальную префиксную сумму
    min_pref_sum = min(min_pref_sum, pref_sums[i + 1])

# ответ
print(max_sum)