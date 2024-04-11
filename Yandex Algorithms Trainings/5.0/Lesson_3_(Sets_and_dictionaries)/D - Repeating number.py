# считываем данные
n, k = map(int, input().split())  # количество измерений, расстояние повторения
nums = list(map(int, input().split()))  # массив чисел
nums_dict = dict()  # словарь индексов числа

answer = 'NO'  # ответ
for i in range(n):  # проходим по числам
    if nums[i] in nums_dict.keys() and i - nums_dict[nums[i]] <= k:  # если число уже было и текущее расстояние - предыдущее укладывается в k - ответ YES
        answer = 'YES'
        break
    nums_dict[nums[i]] = i  # сохраняем текущий индекс числа
# ответ
print(answer)