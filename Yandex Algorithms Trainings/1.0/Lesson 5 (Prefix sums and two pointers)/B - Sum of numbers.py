# считываем данные
N, K = map(int, input().split())
cars = list(map(int, input().split()))

# количество наборов машин
answer = 0
# текущая сумма раздвижного окна
cur_sum = 0

lf = 0
# проходим правым указателем по всему массиву, добавляя элемент в cur_sum
for rg in range(N):
    cur_sum += cars[rg]

    # сумма в раздвижном окне равна K
    if cur_sum == K:
        answer += 1

    # если сумма в раздвижном окне > K
    elif cur_sum > K:
        # сдвигаем левый указатель до уменьшения cur_sum <= K
        while cur_sum > K and lf < rg:
            cur_sum -= cars[lf]
            lf += 1
            # сумма в раздвижном окне равна K
            if cur_sum == K:
                answer += 1

# ответ
print(answer)
