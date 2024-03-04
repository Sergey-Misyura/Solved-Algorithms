from collections import Counter

# считываем данные
seq = list(map(int, input().split()))  # последовательность чисел

answer = []  # массив ответа
count = Counter(seq)
for i in range(len(seq)):
    if count[seq[i]] == 1:
        answer.append(seq[i])

print(*answer)