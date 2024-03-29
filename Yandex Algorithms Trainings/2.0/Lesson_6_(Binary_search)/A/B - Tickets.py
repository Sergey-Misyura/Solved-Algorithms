def binSearchRight(lf, rg, check, checkparams):
    """
    Правый бин поиск
    :param lf: левая граница
    :param rg: правая граница
    :param check: функция проверки
    :param checkparams: параметры проверки
    :return: найденное число
    """
    while lf < rg:
        mid = (lf + rg + 1) // 2
        if check(mid, checkparams):
            lf = mid
        else:
            rg = mid - 1
    return lf


def check_tickets(mid, checkparams):
    """
    Функция подсчитывающая получили ли не менее нужны билетов
    :param mid: цена
    :param checkparams: A, B, C, X, K - параметры задачи
    :return: True если получили нужное число, иначе False
    """
    A, B, C, X, K = checkparams
    # если mid лежит на [A,B] тогда подсчитываем с кассовым сбором
    if mid < A or mid > B:
        tickets = X // mid
    else:
        tickets = X // round((mid * (1 + C/100)), 2)
    return tickets >= K

# считываем данные
A, B, C, X, K = map(int, input().split())  # A, B - границы стоимости со сбором, С - процент сбора, X - деньги, K - число билетов
# используем два правых бин поиска: один для цены до границы B, а второй после нее
lf_price = binSearchRight(1, B, check_tickets, (A, B, C, X, K))
rg_price = binSearchRight(B+1, X, check_tickets, (A, B, C, X, K))
# ответ
# если при цене справа от B получили нужное число билетов - выводим rg_price, иначе lf_price
if X // rg_price >= K:
    print(rg_price)
else:
    print(lf_price)

