# считываем данные
N = int(input().strip())

all_know = set()  # множество языков, которые знают все
one_know = set()  # множество языков, которые знают только один человек

# инициализируем оба множества первым человеком
i = int(input().strip())
for _ in range(i):
    lang = input().strip()
    all_know.add(lang)
    one_know.add(lang)

# для каждого нового человека
for _ in range(N - 1):
    i = int(input().strip())
    cur_langs = set()  # множество текущих языков для текущего человека
    # каждый язык добавляем в множества one_know, cur_langs
    for _ in range(i):
        lang = input().strip()
        one_know.add(lang)
        cur_langs.add(lang)
    # обновляем множество all_know как пересечение all_know и cur_langs
    all_know = all_know & cur_langs

# ответ - длины множест и сами множества all_know, one_know
print(len(all_know))
print(*all_know, sep='\n')
print(len(one_know))
print(*one_know, sep='\n')