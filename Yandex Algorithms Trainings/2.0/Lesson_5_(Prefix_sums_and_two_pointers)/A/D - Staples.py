s = input().strip()  # строка скобок
balance = [0] * len(s)  # баланс скобок
now_bal = 0  # текущий баланс
for i in range(len(s)):  # заполняем массив balance
    now_bal += 1 if s[i] == '(' else -1
    balance[i] = now_bal
# считаем ответ варинта "сначала открывающая потом закрывающая скобки", который можно расположить перед, после и внутри строки
answer = (len(s)+1) * (len(s)+2) // 2
prev_zero = -1  # индекс предыдущего нулевого баланса
for pos in range(len(s)):  # считаем ответ для варианта ')(' который ставится на отрезке между нулевыми балансами
    if balance[pos] == 0:
        answer += (pos - prev_zero - 1) * (pos - prev_zero) // 2
        prev_zero = pos  # обновляем prev_zero
# ответ
print(answer)