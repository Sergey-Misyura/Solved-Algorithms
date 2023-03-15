queue = []
command = [[]]

while command[0]!='exit':
    command = input().split()
	
    if command[0]=='push':
        queue.append(command[1])
        print('ok')

    elif command[0]=='pop':
        output = queue.pop(0) if len(queue)!=0 else 'error'
        print(output)

    elif command[0]=='front':
        output = queue[0] if len(queue)!=0 else 'error'
        print(output)
   
    elif command[0]=='size':
        print(len(queue))

    elif command[0]=='clear':
        queue = []
        print('ok')

    elif command[0]=='exit':
        print('bye')