# считываем данные
n = int(input().strip())  # количество людей
_ = input()  # число песен первого человека
answer = set(input().split())  # множество ответа
# проходим по остальным людям
for _ in range(n - 1):
    _ = input()
    answer = answer.intersection(set(input().split()))  # пересекаем с ответом
# ответ
print(len(answer))
print(*sorted(answer))