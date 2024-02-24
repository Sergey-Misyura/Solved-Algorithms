from collections import defaultdict

# считываем данные
N, K = map(int, input().split())  # N - деревьев, K - сортов
trees = list(map(int, input().split()))  # массив деревьев

# множество обязательных уникальных цветов деревьев
uniq_trees = set()
for i in range(1, K+1):
    uniq_trees.add(i)

# счетчик деревьев помимо обязательных
counter_trees = defaultdict(int)

# указатели ответа и минимальная дистанция
best_lf, best_rg, min_dist = -1, -1, float('inf')

lf = 0  # левая граница окна
# проходимся правым указателем раздвижного окна по массиву
for rg in range(N):
    # если дерево находится в обязательных - убираем, иначе добавляем счетчик лишних
    if trees[rg] in uniq_trees:
        uniq_trees.remove(trees[rg])
    else:
        counter_trees[trees[rg]] += 1

    # когда нашли все подходящие деревья
    if len(uniq_trees) == 0:
        # сдвигаем левую границу пока есть все уникальные сорта деревьев
        while lf <= rg and len(uniq_trees) == 0:
            # меняем ответ при меньшей дистанции
            if min_dist > rg - lf:
                min_dist = rg - lf
                best_lf = lf
                best_rg = rg
            # если убираемое дерево в счетчике - уменьшаем счетчик
            if counter_trees[trees[lf]] > 0:
                counter_trees[trees[lf]] -= 1
            # иначе добавляем во множество необходимых
            else:
                uniq_trees.add(trees[lf])
            lf += 1

# ответ 
print(best_lf + 1, best_rg + 1)