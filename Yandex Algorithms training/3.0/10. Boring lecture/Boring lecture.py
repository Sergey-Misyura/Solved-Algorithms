from collections import defaultdict

word = input()
d = defaultdict(int)
len_word = len(word)
for idx, letter in enumerate(word):
    d[letter]+=(idx+1)*(len_word-idx)

for elem in sorted(d.items()):
    print(f'{elem[0]}:', elem[1])