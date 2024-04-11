class Unit:
    """
    Класс устройства сети
    """
    units = []  # массив всех устройств
    all_updates = []  # счетчик общего количество сделанных обновлений для всех устройств

    def __init__(self, n, k):
        self.number = len(Unit.units)  # номер устройства
        self.updates = [False] * k  # массив частей обновления для текущего устройства
        self.importance = [0] * n  # массив значимости других устройство для текущего
        self.updates_parts = 0  # счетчик числа частей обновления
        self.next_update = -1  # текущая необходимая часть обновления
        self.in_requests = []  # массив запросов к этому устройству
        self.can_update = False  # флаг о возможности выполнить запрос на часть обновления от запрашиваемого устройства
        self.update_from = -1  # номер устройства, которому направлен запрос
        self.timeslots = 0  # счетчик таймслотов для обновления устройства
        Unit.units.append(self)

    def select_part(self):
        """
        Функция выбора запрашиваемой части обновления
        :return: изменяет self.next_update или self.timeslots
        """
        self.next_update = -1  # необходимая часть обновления
        cur_part_updates = float('inf')  # число всех сделанных обновлений по необходимой части
        for i in range(len(self.updates)):  # проходим по массиву обновлений
            if not self.updates[i] and Unit.all_updates[i] < cur_part_updates:  # если нет обновления и обновлений сделано меньше чем cur_part_updates
                self.next_update = i  # обновляем необходимую часть обновления
                cur_part_updates = Unit.all_updates[i]  # обновляем число обновлений по ней
        if self.next_update != -1:  # если еще нужна часть обновления - увеличиваем счетчик таймслотов
            self.timeslots += 1

    def select_unit_update_from(self):
        """
        Функция выбора устройства для запроса на получение обновления
        :return: изменяет список in_requests у устройства c запрашиваемым обновлением
        """
        if self.next_update == -1:  # если обновлений не нужно - возврат
            return
        cur_unit_from = None  # номер устройства для отправления запроса
        cur_unit_from_updates = float('inf')  # число загруженных обновлений на запрашиваемом устройстве
        for cur_unit in Unit.units:  # проходим по всем устройствам
            if cur_unit.updates[self.next_update]:  # если у устройства есть такое обновление
                if cur_unit.updates_parts < cur_unit_from_updates:  # и если число обновлений на устройстве меньше cur_unit_from_updates
                    cur_unit_from = cur_unit  # обновляем запрашиваемое устройство
                    cur_unit_from_updates = cur_unit.updates_parts  # обновляем число обновлений на нем
        if cur_unit_from:  # если нашли устройство
            cur_unit_from.in_requests.append(self)  # добавляем запрос в список запросов устройства cur_unit_from

    def select_request_in(self):
        """
        Функция, выбирающая из всех запросов к текущему устройству-получателю запроса, запрос для выполнения
        :return: очищает self.in_requests, изменяет у устройства-отправителя запроса can_update и update_from
        """
        minupdates_parts = float('inf')  # число обновлений на устройстве-отправителе
        unit_to = -1  # номер устройства-отправителя, для которого будет выполнен запрос на обновление
        cur_importance = -1  # значимость устройства-отправителя для устройства-получателя
        for i in range(len(self.in_requests)):  # проходим по всем запросам к текущему устройству
            cur_unit = self.in_requests[i]  # выбираем устройство, откуда пришел запрос
            if self.importance[cur_unit.number] > cur_importance:  # если значимость устройства-отправителя запроса выше cur_importance
                unit_to = cur_unit.number  # обновляем номер устройства-отправителя
                minupdates_parts = cur_unit.updates_parts  # сохраняем число обновлений на устройстве-отправителе
                cur_importance = self.importance[cur_unit.number]  # обновляем значимость устройства-отправителя
            elif self.importance[cur_unit.number] == cur_importance:  # иначе, если значимость текущего устройства-отправителя одинакова с текущим cur_importance
                if minupdates_parts > cur_unit.updates_parts:  # если частей обновления на устройстве-отправителе меньше текущего minupdates_parts
                    unit_to = cur_unit.number  # обновляем номер устройства-отправителя
                    minupdates_parts = cur_unit.updates_parts  # сохраняем число обновлений на устройстве-отправителе
        self.in_requests = []  # очищаем список запросов
        if unit_to != -1:  # если устройство для выполнения запроса выбрано
            cur_unit = Unit.units[unit_to]  # сохраняем устройство в cur_unit
            cur_unit.can_update = True  # меняем флаг выполненого запроса для устройства cur_unit на True
            cur_unit.update_from = self.number  # меняем в cur_unit номер устройства выполнившего запрос, на текущее устройство

    def request_confirmed(self):
        """
        Функция выполнения запроса на часть обновления
        :return: обновляем все связанные переменные после части обновления self.updates_parts, self.updates, Unit.all_updates, self.importance, self.can_update
        """
        if self.can_update:  # если запрос выполнен - обновляем данные
            self.updates_parts += 1  # увеличиваем счетчик числа обновлений для устройства
            self.updates[self.next_update] = True  # в массиве updates устройства сохраняем обновление
            Unit.all_updates[self.next_update] += 1  # увеличиваем счетчик общего числа обновлений по текущей части обновления
            self.importance[self.update_from] += 1  # увеличиваем значимость устройства откуда пришло обновление
            self.can_update = False  # меняем флаг выполнения запроса части обновления для следующего запроса


# считываем данные
n, k = map(int, input().split())  # число устройств, число частей обновлений

for i in range(n):  # создаем n устройств
    Unit(n, k)
Unit.all_updates = [1] * k  # создаем общее число обновлений, равное числу обновлений на первом устройстве
Unit.units[0].updates_parts = k  # количество прошедших обновлений для первого устройства
Unit.units[0].updates = [True] * k  # массив прошедших обновлений для первого устройства

all_updated = False  # флаг обновления всех устройств
while not all_updated:  # пока еще все устройства не обновлены
    units_updated = 0  # число устройств с полным обновлением
    for cur_unit in Unit.units:  # проходим по всем устройствам
        if cur_unit.updates_parts == k:  # если у устройства все части обновления - увеличиваем units_updated, переходим к следующему
            units_updated += 1
        else:  # иначе выбираем необходимую часть обновления
            cur_unit.select_part()
    if units_updated == n:  # если все устройства обновлены - выход
        all_updated = True
        break
    for cur_unit in Unit.units:  # проходим по устройствам
        if cur_unit.updates_parts != k:  # если у устройства не все обновления
            cur_unit.select_unit_update_from()  # выбираем устройство для запроса обновления
    for cur_unit in Unit.units:  # проходим по устройствам
        if cur_unit.in_requests:  # выполняем запросы к устройству
            cur_unit.select_request_in()
    for cur_unit in Unit.units:  # проходим по устройствам
        if cur_unit.can_update:  # если возможно выполнить запрос для устройства
            cur_unit.request_confirmed()  # выполняем запрос

print(Unit)
answer = []  # массив ответа
for cur_unit in Unit.units:  # проходим по устройствам
    answer.append(cur_unit.timeslots)  # сохраняем в answer таймслоты

# ответ
print(*answer[1:])