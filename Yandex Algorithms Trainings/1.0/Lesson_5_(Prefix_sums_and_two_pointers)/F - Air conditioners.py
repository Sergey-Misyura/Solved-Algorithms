# считываем данные
n = int(input().strip())  # количество классов в школе
classes = list(map(int, input().split()))  # минимальная мощность кондиционера в ваттах для класса i
conditioners = int(input().strip())  # количество предложенных моделей кондиционеров

price_power = []  # массив (цена, мощность) кондиционеров
for _ in range(conditioners):
    # мощность, цена из input в (цена, мощность)
    b, c = map(int, input().split())
    price_power.append((c, b))

# сортируем данные, сортируем кондиционеры по цене
classes.sort()
price_power.sort()

min_price = 0  # минимальная суммарная стоимость кондиционеров в рублях
cond_idx = 0  # индекс текущего кондиционера
# проходимся  по массиву classes
for i in range(n):
    # пока мощность кондиционера недостаточна - сдвигаем указатель в массиве price_power
    while price_power[cond_idx][1] < classes[i]:
        cond_idx += 1

    # добавляем цену кондиционера в ответ, так как в отсортированном массиве он будет самым дешевым при необходимой мощности
    min_price += price_power[cond_idx][0]

# ответ
print(min_price)
