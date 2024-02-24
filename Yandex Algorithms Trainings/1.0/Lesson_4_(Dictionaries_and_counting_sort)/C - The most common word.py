from collections import defaultdict

# считываем данные
with open('input.txt') as f:
    s = f.read().split()

words = defaultdict(int)  # счетчик частот слов

# добавляем слова в счетчик
for i in range(len(s)):
    words[s[i]] += 1

# сортируем счетчик
ans = sorted(words.items(), key=lambda x: (-x[1], x[0]))
# ответ
print(ans[0][0])


