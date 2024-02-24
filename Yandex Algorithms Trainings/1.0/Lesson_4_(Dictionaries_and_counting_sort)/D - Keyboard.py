# считываем данные
n = int(input().strip())
keys = list(map(int, input().split()))  # массив долговечности
k = int(input().strip())

pushs = list(map(int, input().split()))  # массив нажатий

# подсчитываем долговечность
for push in pushs:
    keys[push - 1] -= 1

# приводим массив долговечности в соответствие условиям вывода
for i in range(n):
    keys[i] = 'YES' if keys[i] < 0 else 'NO'

# ответ
print('\n'.join(keys))


