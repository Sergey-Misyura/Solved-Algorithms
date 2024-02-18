def gensequence(L, x1, d1, a, c, m):
    """
    параметры генерации
    :param L:
    :param x1:
    :param d1:
    :param a:
    :param c:
    :param m:
    :return: сгенерированная последовательность
    """
    seq = [x1]
    d = d1
    for _ in range(L - 1):
        seq.append(seq[-1] + d)
        d = ((a * d + c) % m)
    return seq


def left_bin_search(seq, target):
    """
    левый бинарный поиск
    :param seq: последовательность
    :param target: искомое число
    :return: индекс, либо len(seq) если нашли число меньше
    """
    lf, rg = 0, len(seq) - 1
    while lf < rg:
        mid = (lf + rg) // 2
        if seq[mid] >= target:
            rg = mid
        else:
            lf = mid + 1

    if seq[lf] < target:
        return len(seq)
    return lf


def right_bin_search(seq, target):
    """
    правый бинарный поиск
    :param seq: последовательность
    :param target: искомое число
    :return: индекс, либо len(seq) если нашли число больше
    """
    lf, rg = 0, len(seq) - 1
    while lf < rg:
        mid = (lf + rg) // 2 + 1
        if seq[mid] > target:
            rg = mid - 1
        else:
            lf = mid

    if seq[lf] > target:
        return len(seq)
    return len(seq) - lf - 1


def median_search(seq1, seq2, L):
    """
    функция нахождения медианы двух последовательностей, используется бинаарный поиск по ответу
    :param seq1: последовательность 1
    :param seq2: последовательность 2
    :param L: длина последовательностей
    :return: индекс медианы
    """
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
    x1, d1, a, c, m = map(int, input().split())
    # генерируем и добавляем в массив последовательность
    sequences.append(gensequence(L, x1, d1, a, c, m))

answer = []
# проходимся по всем парам последовательностей
for i in range(N):
    for j in range(i + 1, N):
        answer.append(str(median_search(sequences[i], sequences[j], L)))

# ответ
print('\n'.join(answer))