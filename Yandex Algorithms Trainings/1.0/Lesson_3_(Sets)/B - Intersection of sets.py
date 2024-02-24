# считываем данные
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

# выводим отсортированное пересечение множеств
print(*sorted(list(set(s1) & set(s2))))
