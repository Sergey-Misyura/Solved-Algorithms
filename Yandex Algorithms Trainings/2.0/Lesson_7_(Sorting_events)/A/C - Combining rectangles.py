from collections import namedtuple

EventType = namedtuple('EventType', ['OPENING', 'CLOSING'])(OPENING='OPENING', CLOSING='CLOSING')  # типы событий фигур - открытие, закрытие фигуры

class RectangleEvent:
    """
    Класс события прямоугольника
    """
    def __init__(self, x, yT, yB, event_type):
        self.x = x  # координата х
        self.yT = yT  # координата y верхняя
        self.yB = yB  # координата y нижняя
        self.type = event_type  # тип события из EventType

class IntervalEvent:
    """
    Класс события интервала вертикальной стороны прямоугольника
    """
    def __init__(self, y, event_type):
        self.y = y  # y координата
        self.type = event_type  # тип события из EventType

class Interval:
    """
    Класс вертикальных интервалов по оси y
    """
    def __init__(self, first, last):
        self.first = first  # начало интервала по y
        self.last = last  # конец интервала по y

    def __eq__(self, other):  # переназначение функции сравнении - сравнение интервалов по двум границам
        return self.first == other.first and self.last == other.last

def getIntervalsUnion(intervals):
    """
    Функция считающая общую длину прямой, покрываемой интервалами
    :param intervals: входящий массив вертикальных сторон прямоугольников
    :return: общая длина прямой, покрываемой интервалами
    """
    interval_events = []  # массив событий интервалов
    for interval in intervals:  # проходим по входящим интервалам
        interval_events.append(IntervalEvent(interval.first, EventType.OPENING))  # добавляем в events начало вертикальной границы прямоугольника (yB)
        interval_events.append(IntervalEvent(interval.last, EventType.CLOSING))  # добавляем в events конец вертикальной границы прямоугольника (yT)
    interval_events.sort(key=lambda e: e.y)  # сортируем интервалы по y
    union_length = 0  # общая длина на прямой, покрываемой интервалами
    opened_intervals = 0  # количество начавшихся интервалов
    prev_y = interval_events[0].y  # координата y предыдущего начавшегося интервала
    for event in interval_events:  # проходим по событиям в массиве interval_events
        if opened_intervals > 0:  # если есть открытые интервалы - увеличиваем длину union_length на занятый отрезок
            union_length += event.y - prev_y
        if event.type == EventType.OPENING:  # если интервал начался, увеличиваем число открытых интервалов
            opened_intervals += 1
        elif event.type == EventType.CLOSING:  # если интервал закончился, уменьшаем число откртых интервалов
            opened_intervals -= 1
        prev_y = event.y  # обновляем предыдущий y
    # возвращаем общую длину
    return union_length

if __name__ == "__main__":
    # считываем данные
    rectangles_num = int(input())  # число прямоугольников
    if rectangles_num == 0:  # при нуле прямоугольников - возвращаем 0
        print(0)
    else:  # общий случай
        rectangle_events = []  # массив событий
        for _ in range(rectangles_num):
            xL, yB, xR, yT = map(int, input().split())  # координаты x левый, y нижний, x правый, y верхний
            rectangle_events.append(RectangleEvent(xL, yT, yB, EventType.OPENING))  # добавляем в events левую вертикальную границу прямоугольника
            rectangle_events.append(RectangleEvent(xR, yT, yB, EventType.CLOSING))  # добавляем в events правую вертикальную границу прямоугольника
        rectangle_events.sort(key=lambda e: e.x)  # сортируем вертикальные границы по х
        union_area = 0  # площадь объединения
        opened_rectangles = 0  # начавшиеся прямоугольники
        prev_x = rectangle_events[0].x  # x координата пердыдущего прямоугольника
        present_intervals = []  # текущие интервалы вертикальных сторон прямоугольников
        for event in rectangle_events:  # проходим по массиву событий
            # если есть начавшиеся прямоугольники, прямоугольники по х пересеклись -
            # считаем изменение площади пересечения, как изменение координаты х * длину, покрываемую сторонами по y до события event
            # увеличиваем площадь объединения всех прямоугольников
            if opened_rectangles > 0:
                union_area += (event.x - prev_x) * getIntervalsUnion(present_intervals)
            if event.type == EventType.OPENING:  # если прямоугольник начинается
                opened_rectangles += 1  # увеличиваем счетчик начавшихся прямоугольников
                present_intervals.append(Interval(event.yB, event.yT))  # добавляем в текущие интервалы, интервал по вертикальной стороне прямоугольника
            elif event.type == EventType.CLOSING:  # если прямоугольник закончился
                opened_rectangles -= 1  # уменьшаем счетчик начавшихся прямоугольников
                present_intervals.remove(Interval(event.yB, event.yT))  # убираем из текущих интервалов, интервал по вертикальной стороне прямоугольника
            prev_x = event.x  # обновляем x предыдущего прямоугольника

        # ответ
        print(union_area)