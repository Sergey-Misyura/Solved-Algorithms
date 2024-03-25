# считываем данные
P = int(input().strip())  # периметр треугольника
# для большей площади треугольника необходимы стороны, ближайшие к стронам равностороннего треугольника
a = P // 3  # первая из сторон
b = (P - a) // 2  # вторая из сторон
c = P - a - b  # оставшаяся, третья сторона по P периметру
# если неравенство треугольника не выполняется - ответ -1
if a + b <= c:
    print(-1)
# иначе выводим получившиеся стороны, также мы можем найти второй треугольник
else:
    print(a, b, c)
    # для минимальной площади необходим треугольник с наименьшей стороной
    d = 1 if P % 2 == 1 else 2  # при нечетном периметре - минимальная сторона 1, при четном - 2
    e = (P - d) // 2  # следующая сторона
    f = P - d - e  # оставшаяся, третья сторона по P периметру
    # выводим второй треугольник
    print(d, e, f)
