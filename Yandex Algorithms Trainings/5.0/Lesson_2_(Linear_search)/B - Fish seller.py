# считываем данные
N, K = map(int, input().split())  # количество дней, продолжительность хранения
prices = list(map(int, input().split()))  # цена в каждый из дней

max_profit = 0  # максимальная прибыль
for i in range(N - 1):
    # обновляем максимальную прибыль, как максимум из нее и разницы максимума на отрезке от i длиной K и текущего значения цены
    max_profit = max(max_profit, max(prices[i:i+K+1]) - prices[i])
# ответ
print(max_profit)