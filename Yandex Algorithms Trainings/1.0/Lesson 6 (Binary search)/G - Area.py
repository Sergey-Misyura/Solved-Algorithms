n = int(input().strip())  # ширина площади
m = int(input().strip())  # длина площади
t = int(input().strip())  # количество имеющихся плиток

lf, rg = 0, max(n//2, m//2)  # границы бин поиска - от 0 до половины большей стороны
# правый бин поиск
while lf < rg:
    # считаем центр
    mid = (lf + rg) // 2 + 1
    # считаем количество плитки при mid ширине
    count = (mid * 2 * n) + ((m - 2 * mid) * 2 * mid)
    # если уложились, сдвигаем lf на mid
    if count <= t:
        lf = mid
    # иначе сдвигаем rg на mid - 1
    else:
        rg = mid - 1

# ответ
print(lf)