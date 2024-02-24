# считываем данные
s = list(map(int, input().split()))

# если строка не пуста
if s:
    # убираем дубли
    st = set(s)
    # ответ
    print(len(st))
# иначе ответ 0
else:
    print(0)