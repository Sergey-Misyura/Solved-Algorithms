# необходимо для прохождения тестов в контесте
# from sys import set_int_max_str_digits
# set_int_max_str_digits(5000)

mods = [10**9+7, 10**9+11, 10**9+13]  # модули для подсчета хеша
max_fib_num = 40000  # предел количества чисел Фибоначчи

fib_hashes = []  # массив множеств хешей по модулям
for _ in range(len(mods)):
    fib_hashes.append(set())

# подсчитываем хеши чисел Фибоначчи по каждому модулю, добавляем в fib_hashes
for i in range(len(mods)):
    f1, f2 = 1, 1
    fib_hashes[i].add(1)
    for j in range(max_fib_num):
        f1, f2 = f2, (f1 + f2) % mods[i]
        fib_hashes[i].add(f2)

n = int(input())  # числов запросов
answer = []  # массив ответов
# для каждого запроса
for i in range(n):
    cur = int(input())  # текущее число
    is_fib = True  # флаг - является ли числом Фибоначчи
    # проверяем массив множеств хешей fib_hashes на наличие хеша текущего числа
    for j in range(len(mods)):
        # флаг остается True если во всех множествах был хеш
        is_fib = is_fib and cur % mods[j] in fib_hashes[j]
    # если флаг True - ответ Yes
    if is_fib:
        answer.append('Yes')
    # инча ответ No
    else:
        answer.append('No')

# выводим ответ
print(*answer, sep='\n')