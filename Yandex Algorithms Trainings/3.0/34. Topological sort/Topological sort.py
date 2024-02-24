import sys
sys.setrecursionlimit(1000000)

N, M = tuple(map(int,input().split()))
graph_list = [[] for _ in range(N+1)]
   
for i in range(M):
    v1, v2 = tuple(map(int,input().split()))
    graph_list[v1].append(v2)

if N==1:
    print(-1)
elif M==0:
    print(' '.join([str(i) for i in range(1,N+1)]))
else:
   
    visited = [0 for _ in range(N+1)]
    vertexes = []
   
    def dfs(now):
        visited[now] = 1
        for neigh in graph_list[now]:
            if visited[neigh] == 0:
                dfs(neigh)
            elif visited[neigh] == 1:
                print(-1)
                sys.exit()
        visited[now] = 2
        vertexes.append(now)
        return
   
    for i in range(1, N+1):
        if visited[i]==0:
            dfs(i)
    print(*vertexes[::-1])