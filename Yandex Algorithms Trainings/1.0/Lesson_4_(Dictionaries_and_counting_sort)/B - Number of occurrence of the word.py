from collections import defaultdict

# считываем данные
with open('input.txt') as f:
    s = f.read().split()

words = defaultdict(int)  # счетчик появления слов
ans = [0]*len(s)  # массив ответа

# проходим по s
for i in range(len(s)):
    # записываем в ответ частоту появлений слова из счетчика
    ans[i] = words[s[i]]
    # увеличиваем счетчик
    words[s[i]] += 1

# ответ
print(*ans)

