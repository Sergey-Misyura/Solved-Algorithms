def fbinSearch(lf, rg, eps, check, checkparams):
    """
    Функция бинарного поиска для вещественных чисел
    :param lf: левая граница
    :param rg: правая граница
    :param eps: точность
    :param check: функция проверки
    :param checkparams: параметры функции проверки
    :return: число, на котором сошелся бинарный поиск
    """
    while lf + eps < rg:
        mid = (lf + rg) / 2
        if check(mid, checkparams):
            rg = mid
        else:
            lf = mid
    return lf


def check_pos(x, params):  # функция, считающая значение кубического уравнения, определяет приблежение к 0 с положительной части
    a, b, c, d = params
    return a * x**3 + b * x**2 + c * x + d > 0

def check_neg(x, params):  # функция, считающая значение кубического уравнения, определяет приблежение к 0 с отрицательной части
    a, b, c, d = params
    return a * x**3 + b * x**2 + c * x + d < 0

# считываем данные
a, b, c, d = map(int, input().split())  # коэффициенты кубического уравнения
eps = 0.000001  # точность поиска
# если коэффициент a положительный - в функции проверки бин поиска используем check_pos, иначе check_neg
if a > 0:
    print(fbinSearch(-1000000, 1000000, eps, check_pos, (a, b, c, d)))
else:
    print(fbinSearch(-1000000, 1000000, eps, check_neg, (a, b, c, d)))