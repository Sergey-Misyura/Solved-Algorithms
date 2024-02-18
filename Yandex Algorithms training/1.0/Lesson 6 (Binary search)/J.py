# левый бин поиск
def left_bin_search(seq, target):
    lf, rg = 0, len(seq) - 1
    while lf < rg:
        mid = (lf + rg) // 2
        if seq[mid] >= target:
            rg = mid
        else:
            lf = mid + 1

    # если мы не нашли target возвращаем длину для невыполнения условия в поиске медианы
    if seq[lf] < target:
        return len(seq)
    return lf


# правый бин поиск
def right_bin_search(seq, target):
    lf, rg = 0, len(seq) - 1
    while lf < rg:
        mid = (lf + rg) // 2 + 1
        if seq[mid] > target:
            rg = mid - 1
        else:
            lf = mid

    # если мы не нашли target возвращаем длину для невыполнения условия в поиске медианы
    if seq[lf] > target:
        return len(seq)
    return len(seq) - lf - 1


# бин поиск по ответу
def median_search(seq1, seq2, L):
    lf = min(seq1[0], seq2[0])
    rg = max(seq1[-1], seq2[-1])
    while lf < rg:
        mid = (lf + rg) // 2
        # считаем левым и правым бинпоиском количество меньше и больше mid
        less = left_bin_search(seq1, mid) + left_bin_search(seq2, mid)
        great = right_bin_search(seq1, mid) + right_bin_search(seq2, mid)
        # если нашли mid, возвращаем его
        if less <= L - 1 and great <= L:
            return mid
        # иначе, если элементов больших mid > L, двигаем lf
        elif great > L:
            lf = mid +1
        # иначе, если элементов меньших mid > L - 1, двигаем rg
        elif less > L - 1:
            rg = mid - 1

    return lf

# считываем данные
N, L = map(int, input().split())
sequences = []
for _ in range(N):
    sequences.append(list(map(int, input().split())))

answer = []
# проходимся по всем парам последовательностей
for i in range(N):
    for j in range(i + 1, N):
        answer.append(str(median_search(sequences[i], sequences[j], L)))

# ответ
print('\n'.join(answer))