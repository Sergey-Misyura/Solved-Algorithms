from math import ceil


def binSearchLeft(lf, rg, check, target):  # левый бин поиск числа выполняемых задач в день
    while lf < rg:
        mid = (lf + rg) // 2
        if check(mid, target):
            rg = mid
        else:
            lf = mid + 1
    return lf


def check_days(m, target):
    days = [ceil(tasks / m) for tasks in projects]  # число затрачиваемых дней при выполнении m задач в день
    return sum(days) <= target


# считываем данные
T = int(input().strip())  # дней до дедлайна
projects = list(map(int, input().split()))  # список задач проектов
answer = binSearchLeft(1, max(projects), check_days, T)  # ответ - левый бин поиск по ответу
# ответ
print(answer)
