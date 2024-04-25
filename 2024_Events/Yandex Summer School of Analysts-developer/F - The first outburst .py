from math import ceil
import bisect

# считываем данные
with open('input.txt', 'r') as f:
    N = int(f.readline())  # всего отсчетов
    K = int(f.readline())  # первые дни без выбросов
    signals = list(map(int, f.readline().split()))  # массив сигналов

seen = sorted(signals[0:K])  # сортируем первые K и добавляем в seen
idx = -2  # индекс первого выброса
for i in range(K, N):  # проходим по оставшимся сигналам в signals
    signal = signals[i]  # текущий сигнал
    if len(signals) == 1:  # частный случай если всего два сигнала
        idx = i if signal > signals[0] else idx  # выброс второй сигнла, либо нет
    elif idx == -2:  # иначе, если ндекс не найден
        if signal <= seen[ceil(0.9 * i) - 1]:  # если сигнал не выброс - добавляем через бинпоиск в seen
            bisect.insort(seen, signal)
        else:  # иначе записываем индекс в ответ
            idx = i
            break
# ответ - сам номер сигнала или -1
print(idx + 1)
