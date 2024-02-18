N, K = map(int, input().split())
wires = []
for _ in range(N):
    wires.append(int(input().strip()))

if sum(wires) < K:
    # отдельнообрабатываемый случай
    print(0)
else:
    # не обязательно все провода делить, поэтому rg = max(wires)
    lf, rg = 0, max(wires)
    # правый бин поиск
    while lf < rg:
        # считаем центр
        mid = (lf + rg) // 2 + 1
        # считаем количество частей
        count = sum([wire // mid for wire in wires])
        # если не менее K, сдвигаем lf на mid
        if count >= K:
            lf = mid
        # иначе сдвигаем rg на mid - 1
        else:
            rg = mid - 1

    # ответ
    print(lf)