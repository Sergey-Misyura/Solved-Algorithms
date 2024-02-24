deque = []
command = [[]]

while command[0]!='exit':
    command = input().split()

    if command[0]=='push_front':
        deque.insert(0, command[1])
        print('ok')

    if command[0]=='push_back':
        deque.append(command[1])
        print('ok')

    elif command[0]=='pop_front':
        output = deque.pop(0) if len(deque)!=0 else 'error'
        print(output)

    elif command[0]=='pop_back':
        output = deque.pop() if len(deque)!=0 else 'error'
        print(output)

    elif command[0]=='front':
        output = deque[0] if len(deque)!=0 else 'error'
        print(output)

    elif command[0]=='back':
        output = deque[-1] if len(deque)!=0 else 'error'
        print(output)
   
    elif command[0]=='size':
        print(len(deque))

    elif command[0]=='clear':
        deque = []
        print('ok')

    elif command[0]=='exit':
        print('bye')