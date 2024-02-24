clients = dict()  # клиенты банка

# считываем данные
with open('input.txt') as f:
    # для каждой операции из строки файла
    for line in f.readlines():
        operation = list(line.split())

        # если необходим Баланс
        if operation[0] == 'BALANCE':
            # если человека нет среди клиентов - Ошибка
            if operation[1] not in clients.keys():
                print('ERROR')
            # иначе - печатаем Баланс
            else:
                print(clients[operation[1]])
        # для других операций
        else:
            # если человека нет среди клиентов - создаем 0 счет
            if operation[1] not in clients.keys():
                clients[operation[1]] = 0

            # для операции Депозит - увеличиваем счет клиента
            if operation[0] == 'DEPOSIT':
                clients[operation[1]] += int(operation[2])
            # для операции снятие - уменьшаем счет клиента
            elif operation[0] == 'WITHDRAW':
                clients[operation[1]] -= int(operation[2])
            # для операции Перевод
            elif operation[0] == 'TRANSFER':
                # если второго человека нет среди клиентов - создаем 0 счет
                if operation[2] not in clients.keys():
                    clients[operation[2]] = 0

                # производим Перевод
                amount = int(operation[3])
                clients[operation[1]] -= amount
                clients[operation[2]] += amount
            # для операции Начисление процента
            elif operation[0] == 'INCOME':
                p = int(operation[1])
                # если человек есть среди клиентов и если баланс не нулевой - начисляем процент
                for client in clients.keys():
                    if clients[client] > 0:
                        clients[client] = int(clients[client]*(1+p/100))

