from collections import defaultdict

# считываем данные
n, k = map(int, input().split())  # n – количество символов в строке, k - максимальное число повторов слова
s = input().strip()  # данная строка

# счетчик повторений букв в подстроке
c_counter = defaultdict(int)

# сохраняем максимальное количество повторений символа среди всех символов для сравнения его с k
# и сам символ, так как для уменьшения max_value необходимо найти именно его
max_value = 0
max_c = s[0]  # символ с max_value
# начало подстроки ответа и длина подстроки ответа
best_lf, best_len = -1, -1

lf = 0  # левый указатель раздвижного окна
# проходим правым указателем раздвижного окна по строке
for rg in range(n):
    # увеличиваем счетчик повторений букв
    c_counter[s[rg]] += 1
    # сравниваем max_value c счетчиком, если счетчик больше - обновляем max_value и max_c
    if c_counter[s[rg]] > max_value:
        max_value = c_counter[s[rg]]
        max_c = s[rg]

    # если насчитали max_value не больше k символов, обновляем ответ
    if max_value <= k:
        best_len = rg - lf + 1
        best_lf = lf
    # иначе сдвигаем указатель lf окна, ища символ max_c, для уеньшения max_value до k
    else:
        while max_value > k and lf < rg:
            c_counter[s[lf]] -= 1
            if s[lf] == max_c:
                max_value -= 1
            lf += 1
# ответ
print(best_len, best_lf+1)




