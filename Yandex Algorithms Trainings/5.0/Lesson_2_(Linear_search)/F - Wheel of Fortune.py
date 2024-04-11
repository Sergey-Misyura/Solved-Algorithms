# считываем данные
n = int(input().strip())  # количество секторов колеса
sectors = list(map(int, input().split()))  # массив значений секторов
a, b, k = map(int, input().split())  # мин скорость колеса, макс скорость колеса, скорость замедления

max_prize = 0  # максимальный приз
passed_sectors, rem = divmod(a, k)  # пройденные сектора, остаток
if rem == 0:  # если остаток = 0, значит последний сектор не прошли, уменьшаем на 1
    passed_sectors -= 1
clockwise = passed_sectors % n  # убираем пройденные круги
max_prize = max(sectors[clockwise], sectors[- clockwise])  # обновляем max_prize
# проходим по скоростям, каждый раз увеличивая на k, то есть переходим к следующему сектору
# проверяем только 1 прокрутку колеса, функцией min убирая лишние циклы вращения
for cur_speed in range(a+k, min(b+1, a+n*k+1), k):
    clockwise += 1  # увеличиваем место остановки
    if clockwise == n:  # если сделали оборот возвращаемся в начальную точку
        clockwise = 0
    max_prize = max(max_prize, sectors[clockwise], sectors[- clockwise])  # обновляем max_prize
# ответ
print(max_prize)
