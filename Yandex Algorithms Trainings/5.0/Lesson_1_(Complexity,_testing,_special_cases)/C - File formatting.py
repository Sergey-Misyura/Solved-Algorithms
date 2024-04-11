# считываем данные
n = int(input().strip())  # число строк
cum_count = 0  # кумулятивное количество нажатий

for _ in range(n):
    added_spaces = int(input().strip())  # добавляемые пробелы
    tabs, spaces = divmod(added_spaces, 4)  # количество нажатий tab и space
    cum_count += tabs  # добавляем количество tab
    cum_count += spaces if spaces != 3 else 2  # добавляем число пробелов если != 3, иначе 3 меняем на 2 (tab + backspace)
# ответ
print(cum_count)