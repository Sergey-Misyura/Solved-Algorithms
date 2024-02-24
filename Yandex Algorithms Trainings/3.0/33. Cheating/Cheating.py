N, M = tuple(map(int,input().split()))
if M==0:
    print('YES')
else:
    graph_list = [[] for _ in range(N+1)]
    for i in range(M):
        v1, v2 = tuple(map(int,input().split()))
        graph_list[v1].append(v2)
        graph_list[v2].append(v1)
   
     
    visited = [0 for _ in range(N+1)]
    group_nums = (0, 2, 1)
    answer = ''
   
    def dfs(now, num):
        visited[now] = num
        for neig in graph_list[now]:
            if visited[neig]==0:
                dfs(neig, group_nums[num])
            elif visited[neig]==num:
                global answer
                answer = 'NO'
                break
   
    for i in range(1,N+1):
        if visited[i] != [] and visited[i]==0:
            dfs(i, 1)

    if answer=='NO':
        print('NO')
    else:
        print('YES')