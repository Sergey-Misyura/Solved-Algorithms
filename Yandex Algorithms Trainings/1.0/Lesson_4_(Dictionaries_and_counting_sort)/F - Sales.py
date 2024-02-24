from collections import defaultdict

# словарь счетчиков покупок для каждого покупателя
# вида: {покупатель1: {покупка1: количество, покупка2: количество}}
purchases = defaultdict(lambda: defaultdict(int))

# считываем данные и добавляем в purchases
with open('input.txt') as f:
    for line in f.readlines():
        buyer, product, count = line.split()
        count = int(count)

        purchases[buyer][product] += count

# ответ - выводим отсортированный словарь purchases с отсортированными внутренними словарями
for buyer, products in sorted(purchases.items()):
    print(buyer, ':', sep='')
    for product, count in sorted(products.items()):
        print(product, count)



