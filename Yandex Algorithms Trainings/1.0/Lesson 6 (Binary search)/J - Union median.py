def left_bin_search(seq, target):
    """
    Левый бинарный поиск
    :param seq: последовательность
    :param target: искомое число
    :return: индекс найденного числа, либо len(seq) если нашли число меньше
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
    Правый бинарный поиск
    :param seq: последовательность
    :param target: искомое число
    :return: индекс найденного числа, либо len(seq) если нашли число больше
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
    Функция нахождения медианы двух последовательностей, используется бинаарный поиск по ответу
    :param seq1: последовательность 1
    :param seq2: последовательность 2
    :param L: длина последовательностей
    :return: левая медиана двух последовательностей
    """
    lf = min(seq1[0], seq2[0])
    rg = max(seq1[-1], seq2[-1])
    while lf < rg:
        mid = (lf + rg) // 2
        # считаем левым и правым бинпоиском количество элементов меньше и больше mid
        less = left_bin_search(seq1, mid) + left_bin_search(seq2, mid)
        great = right_bin_search(seq1, mid) + right_bin_search(seq2, mid)
        # если нашли mid, возвращаем его
        if less <= L - 1 and great <= L:
            return mid
        # иначе, если элементов больших mid > L, двигаем lf в mid +1
        elif great > L:
            lf = mid +1
        # иначе, если элементов меньших mid > L - 1, двигаем rg в mid - 1
        elif less > L - 1:
            rg = mid - 1

    # возвращаем левую медиану двух последовательностей
    return lf

# считываем данные
N, L = map(int, input().split())  # N - последовательностей по L - элементов
sequences = []  # последовательности
for _ in range(N):
    sequences.append(list(map(int, input().split())))

answer = []  # ответ
# проходимся по всем парам последовательностей
for i in range(N):
    for j in range(i + 1, N):
        # добавляем в ответ левую медиану последовательностей
        answer.append(str(median_search(sequences[i], sequences[j], L)))

# ответ
print('\n'.join(answer))