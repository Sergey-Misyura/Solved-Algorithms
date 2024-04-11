# одномерная преф сумма не проходит по времени на Python, следует использовать двумерную
# одномерная переписана на Cpp, на нем проходит

def binSearchRight(lf, rg, check, region, n, m):  # функция левого бин поиска
    while lf < rg:
        mid = (lf + rg + 1) // 2
        if check(mid, region, n, m):
            lf = mid
        else:
            rg = mid - 1
    return lf


def check_region(size, region, n, m):  # функция проверки участка
    for row in range(size, n - 2 * size + 1):  # проходим по строкам для центрального квадрата
        for col in range(size * 2 - 1, m - size):  # проходим по столбцам для центрального квадрата
            if region[row][col + size] >= size * 3:  # если в текущей строке в последнем блоке хватает места как size * 3
                build = True  # флаг возможности построить
                # проверяем верхнюю часть креста
                build_row = row - size  # текущая строка верхней части креста
                while build and build_row < row:  # проходим по строкам верхней части креста, пока флаг True
                    if region[build_row][col] < size:  # если блоков не хватило - флаг False
                        build = False
                    build_row += 1
                # проверяем среднюю часть креста
                build_row = row + 1  # текущая строка средней части креста (1 строку мы уже проверили, поэтому row + 1)
                while build and build_row < row + size:  # проходим по строкам средней части креста, пока флаг True
                    if region[build_row][col + size] < size * 3:  # если блоков не хватило - флаг False, здесь size * 3, потому чо 3 блока стороны size
                        build = False
                    build_row += 1
                # проверяем нижнюю часть креста
                build_row = row + size  # текущая строка нижней части креста
                while build and build_row < row + size * 2:  # проходим по строкам нижней части креста, пока флаг True
                    if region[build_row][col] < size:  # если блоков не хватило - флаг False
                        build = False
                    build_row += 1
                # если возможно построить - возвращаем True
                if build:
                    return True
    # если не построили - возвращаем False
    return False


# считываем данные
with open('input.txt', 'r') as f:
    n, m = map(int, f.readline().split())  # длина и ширина участка под застройку
    region = []  # массив участка под застройку, он же массив преф сумм
    max_len = 0  # максимальная длина подряд идущих # по горизонтале
    for _ in range(n):
        row = list(f.readline().strip())
        row[0] = 0 if row[0] == '.' else 1  # заменяем '.' на 0, '#' на 1

        for i in range(1, m):  # проходим по строке, преобразуя ее, в ней считаем преф суммы подряд идущих #, обновляем max_len
            row[i] = 0 if row[i] == '.' else row[i - 1] + 1
            max_len = max(max_len, row[i])
        region.append(row)
# находим одвет левым бинпоиском, правая граница выбирается как минимум из высоты, ширины и max_len, потом делится на 3
answer = binSearchRight(1, (min(n, m, max_len)) // 3, check_region, region, n, m)
# ответ
print(answer)