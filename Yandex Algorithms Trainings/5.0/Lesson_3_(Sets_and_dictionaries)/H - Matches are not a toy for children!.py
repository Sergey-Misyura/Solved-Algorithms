from collections import defaultdict, Counter

# считываем данные
with open('input.txt', 'r') as f:
    N = int(f.readline().strip())  # количество спичек
    vecs_dict = defaultdict(list)  # словарь исходных положений спичек вида - вектор: массив начал спичек с таким вектором
    for _ in range(N):  # заполняем vecs_dict
        x1, y1, x2, y2 = map(int, f.readline().split())
        if x1 < x2 or (x1 == x2 and y1 < y2):  # выбираем началом вектора левый х, при одинаковых значениях - нижний y
            vecs_dict[(x2 - x1, y2 - y1)].append((x1, y1))
        else:
            vecs_dict[(x1 - x2, y1 - y2)].append((x2, y2))

    vecs_target_dict = defaultdict(list)  # словарь целевых положений спичек вида - вектор: массив мачал спичек с таким вектором
    for _ in range(N):  # заполняем vecs_target_dict
        x1, y1, x2, y2 = map(int, f.readline().split())
        if x1 < x2 or (x1 == x2 and y1 < y2):  # выбираем началом вектора левый х, при одинаковых значениях - нижний y
            vecs_target_dict[(x2 - x1, y2 - y1)].append((x1, y1))
        else:
            vecs_target_dict[(x1 - x2, y1 - y2)].append((x2, y2))

ident_vectors = set(vecs_dict.keys()) & set(vecs_target_dict.keys())  # находим общие вектора для исходного и целевого положений
if len(ident_vectors) == 0:  # если общих векторов нет - ответ 0
    print(N)
else:  # иначе подсчитываем вектора которые можем перенести
    # идея решения - для спичек с общим вектором, определяем по каким векторам переносится каждая спичка из исходного массива к каждой спичке в целевой массив
    # далее считаем какой вектор перенесет больше всего спичек, ответ разница между N и перенесенными спичками
    bias_vectors = []  # общий массив векторов переноса
    for cur_vec in ident_vectors:  # проходим по каждому общему вектору из ident_vectors
        for cur_target in vecs_target_dict[cur_vec]:  # проходим по списку начал для общего вектора cur_vec в vecs_target_dict
            for cur_from in vecs_dict[cur_vec]:  # проходим по списку начал для общего вектора cur_vec в vecs_dict
                # считаем вектор переноса от cur_from до cur_target, добавляем в массив векторов переноса
                bias_vectors.append((cur_target[0] - cur_from[0], cur_target[1] - cur_from[1]))
    # подсчитаем количество повторений векторов переноса
    counts = Counter(bias_vectors)
    # ответ: N - макс число векторов переноса
    print(N - counts.most_common(1)[0][1])
