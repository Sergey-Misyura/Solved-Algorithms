# считываем данные
seq1 = list(map(int, input().split()))
seq2 = list(map(int, input().split()))

# ответ - длина пересечения множеств чисел в каждой последовательности
print(len(set(seq1) & set(seq2)))