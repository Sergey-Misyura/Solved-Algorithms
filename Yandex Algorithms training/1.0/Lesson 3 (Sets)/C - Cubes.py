# считываем данные
N, M = map(int, input().split())
a = set()
b = set()

for i in range(N):
    a.add(int(input().strip()))

for i in range(M):
    b.add(int(input().strip()))

inter = a & b  # пересечение множеств
a = a - inter  # остаток от первого множества - пересечение
b = b - inter  # остаток от второго множества - пересечение

# ответ - длины, множества
print(len(inter))
print(*sorted(inter))
print(len(a))
print(*sorted(a))
print(len(b))
print(*sorted(b))


