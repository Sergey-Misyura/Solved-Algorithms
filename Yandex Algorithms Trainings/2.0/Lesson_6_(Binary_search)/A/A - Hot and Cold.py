lf_x = 0  # левая граница бин поиска x
rg_x = 10**9  # правая граница бин поиска x
while lf_x != rg_x:  # пока бин поиск не сошелся
    print(lf_x, 0)  # проверяем левую границу
    _ = int(input())  # ответ системы
    print(rg_x, 0)  # проверяем правую границу
    answer = int(input())  # ответ системы
    # если правая граница ближе, то переносим левую в mid + 1, иначе переносим правую границу в mid
    if answer == 1:
        lf_x = (rg_x + lf_x) // 2 + 1
    else:
        rg_x = (rg_x + lf_x) // 2

lf_y = 0  # левая граница бин поиска y
rg_y = 1000000000  # правая граница бин поиска y
while lf_y != rg_y:  # пока бин поиск не сошелся
    print(lf_x, lf_y)  # проверяем левую границу
    _ = int(input())  # ответ системы
    print(lf_x, rg_y)  # проверяем правую границу
    answer = int(input())  # ответ системы
    if answer == 1:  # если правая граница ближе, то переносим левую в mid + 1, иначе переносим правую границу в mid
        lf_y = (rg_y + lf_y) // 2 + 1
    else:
        rg_y = (rg_y + lf_y) // 2

# ответ
print("A", lf_x, lf_y)