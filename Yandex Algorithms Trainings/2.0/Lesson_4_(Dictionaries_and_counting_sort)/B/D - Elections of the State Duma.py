from collections import defaultdict

party_voices = defaultdict(int)  # счетчик голосов партий
# считываем данные
total_voices = 0  # количество всех голосов
with open('input.txt') as f:
    # из каждой строки файла добавляем партии и голоса в счетчик, считаем total_voices
    for line in f.readlines():
        seq = list(line.split())
        party = ' '.join(seq[:-1])
        voices = int(seq[-1])
        party_voices[party] += voices
        total_voices += voices


total_places = 0  # общее число занятых мест
party_places = defaultdict(int)  # словарь мест, занятых партиями
rem_list = []  # массив остатков от деления
# так как первого избирательного частное = total_voices / 450, а для вычисления мест необходимо голоса/первоe
# избирательноe частное - заменим деление умножением: число мест - голоса * 450 / общее число голосов
# проходим по счетчику голосов партий
for party, voices in party_voices.items():
    # так как везде делитель одинаковый сохраним остаток от деления в массив rem_list для подсчета оставшихся мест
    places, rem = divmod(voices * 450, total_voices)  # places - места партии, rem - числитель остатка от деления
    party_places[party] = places
    total_places += places
    rem_list.append((rem, voices, party))  # остаток от деление, число голосов за партию, партия

# сортируем массив от максимума к минимуму для правильного установления очереди партий
rem_list.sort(reverse=True)

rem_places = 450 - total_places  # оставшиеся места в парламенте
# если есть нераспределенные места
if rem_places > 0:
    # прроходим по отсортированному массиву rem_list и каждой партии добавляем 1 место
    for i in range(rem_places):
        party = rem_list[i][2]
        party_places[party] += 1
# формируем ответ из party_places и выводим
print(*[' '.join([party, str(places)]) for party, places in party_places.items()], sep='\n')