# считываем данные
days, parties_count = map(int, input().split())  # число дней, количество партий
strikes = set()  # множество забастовок

# проходим по партиям
for i in range(parties_count):
    start, period = map(int, input().split())  # начало забастовок, период забастовок
    # создаем список забастовок, исключая выходные
    strikes_list = [i for i in range(start, days+1, period) if i % 7 != 0 and i % 7 != 6]
    # обновляем множество забастовок
    strikes.update(strikes_list)

# ответ
print(len(strikes))
