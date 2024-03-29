from math import ceil

def wait_bus(start_stop, start_time):  # функция ожидания автобуса
    min_wait = float('inf')  # минимальное время ожидания
    min_wait_route = 0  # маршрут проезда автобуса при min_wait
    for time, period, route in stops[start_stop]:  # проходим по маршрутам для остановки start_stop
        if start_time <= time:  # если время подъезда не больше заданного start_time
            cur_wait = time - start_time  # текущее ожидание - разница времени подъезда и заданного
        else:  # иначе, если время подъезда больше заданного
            cycles = ceil((start_time - time) / period)  # считаем циклы проезда автобуса с округлением к большему
            cur_wait = time + cycles * period - start_time  # считаем текущее время ожидания в зависимости от циклов

        if cur_wait < min_wait:  # если получили меньшее время ождиания - обновляем его и маршрут при нем
            min_wait = cur_wait
            min_wait_route = route
        elif cur_wait == min_wait:  # если полученное время ождания равно уже найденному, выбираем маршрут с меньшим номером
            min_wait_route = min(min_wait_route, route)
    # найденный маршрут проезда, а также обновленное время путешествие: начальное + время ожидания
    return min_wait_route, start_time + min_wait


def trip(bus_route, time):  # функция поездки по маршруту автобуса
    ln_bus_route = len(busses[bus_route])  # длина маршрута автобуса
    # возвращаем остановку приезда
    return busses[bus_route][time % ln_bus_route]

# считываем данные
n, k = map(int, input().split())
busses = dict()  # словарь маршрутов автобусов
stops = [set() for _ in range(n + 1)]  # массив остановок с множеством проходящих по ним маршрутов вида (время пребывания, период, маршрут)
empty_stops = set([i for i in range(1, n + 1)])  # остановки без маршрута
for i in range(1, k + 1):  # проходим по маршрутам автобусов
    cur_bus = list(map(int, input().split()))[1:]
    busses[i] = cur_bus  # сохраняем в busses
    len_cur = len(cur_bus)  # длина текущего маршрута
    for time, stop in enumerate(cur_bus):  # проходим по текущему маршруту
        stops[stop].add((time, len_cur, i))  # добавляем в текущую остановку текущий маршрут
        if empty_stops and stop in empty_stops:  # если остановка была в пустых, убираем оттуда
            empty_stops.remove(stop)

p = int(input().strip())  # число людей
answer = [0] * p  # массив ответа
for i in range(p):  # проходим по плану катания каждого человека
    route = list(map(int, input().split()))
    start = route[0]  # начальная остановка
    route = route[2:]  # массив проежаемых остановок
    if start in empty_stops:  # если к первой остановке нет маршрутов - записываем в answer 0 0
        answer[i] = '0 0'
    else:  # если маршруты есть
        cur_stop = start  # текущая остановка
        journey_time = 0  # время путешествия
        for travel_time in route:  # проходим массиву проежаемых остановок (1 остановка - 1 ед времени)
            bus_route, journey_time = wait_bus(cur_stop, journey_time)  # получаем маршрут на котором поедем, обновляем время путешествия с учетом времени ожидания
            cur_stop = trip(bus_route, journey_time + travel_time)  # получаем текущую остановку после проезда по bus_route
            journey_time += travel_time + 1  # увеличиваем время путешествия

        journey_time -= 1  # убираем последнюю единицу ожидания на остановке
        answer[i] = str(journey_time) + ' ' + str(cur_stop)  # добавляем полученные значения в ответ

# ответ
print(*answer, sep='\n')