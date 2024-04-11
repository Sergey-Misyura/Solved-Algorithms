from collections import Counter

# считываем данные
n = int(input().strip())  # количество чисел
nums = list(map(int, input().split()))  # сами числа

counts = Counter(nums)  # счетчик повторений чисел
sorted_keys = sorted(counts.keys(), reverse=True)  # сортируем ключи
if len(sorted_keys) == 1:  # если числа одинаковы - ответ 0
    print(0)
else:  # если есть разные числа
    # находим стартовое значение удаленных чисел, как минимальное из разницы количества всех чисел и повторения каждого числа
    min_del_nums = min([n - val for val in counts.values()])  # минимальное число удаленных чисел из массива
    for i in range(1, len(sorted_keys)):  # проходим по ключам счетчика
        if abs(sorted_keys[i] - sorted_keys[i - 1]) <= 1:  # если у соседнего слева с текущим разница не более 1
            min_del_nums = min(min_del_nums, n - counts[sorted_keys[i]] - counts[sorted_keys[i - 1]])  # обновляем min_del_nums - из n вычитаем текущий и соседний слева
    # ответ
    print(min_del_nums)
