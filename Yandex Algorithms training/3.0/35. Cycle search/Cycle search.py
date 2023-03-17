N = int(input())
if N<3:
    print('NO')
else:
    graph_matrix = []
    graph_list = [[] for _ in range(N+1)]
    for _ in range(1,N+1):
        graph_matrix.append(list(map(int,input().split())))

    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph_matrix[i-1][j-1]==1:
                graph_list[i].append(j)
   
    cycle = False
   
    def dfs(now, prev):
        global cycle
        global vert_list
        global visited
        global tail
        global full_cycle
        visited[now] = 1
        for neig in graph_list[now]:
            if not cycle:
                if neig!=prev:
                    if visited[neig]==0:
                        dfs(neig, now)
                    elif visited[neig]==1:
                        cycle = True
                        tail = neig
                        break
        if not cycle:
            visited[now] = 2
        else:
            if not full_cycle:
                vert_list.append(now)
            if tail==now:
                full_cycle = True


    i=1
    while i<=N and not cycle:
        visited = [0 for _ in range(N+1)]
        vert_list = []
        full_cycle = False
        dfs(i, 0)
        i+=1
   
    if cycle:
        print('YES')
        print(len(vert_list))
        print(' '.join([str(vert) for vert in vert_list[::-1]]))
    else:
        print('NO')