from collections import defaultdict

N = int(input())

train_dict = defaultdict(int)
train_list = []
for i in range(N):
    command = input().split()

    if command[0] == 'add':
        if train_list == []:
            train_list.append([int(command[1]), command[2]])
        else:
            if train_list[-1][1] == command[2]:
                train_list[-1][0] += int(command[1])
            else:
                train_list.append([int(command[1]), command[2]])

        train_dict[command[2]] += int(command[1])

    if command[0] == 'delete':
        total_del = int(command[1])

        while total_del != 0:
            if train_list[-1][0] > total_del:
                train_list[-1][0] -= total_del
                train_dict[train_list[-1][1]] -= total_del
                total_del = 0
            else:
                cur = train_list.pop()
                train_dict[cur[1]] -= cur[0]
                total_del -= cur[0]

    if command[0] == 'get':
        if command[1] not in train_dict.keys():
            print(0)
        else:
            print(train_dict[command[1]])