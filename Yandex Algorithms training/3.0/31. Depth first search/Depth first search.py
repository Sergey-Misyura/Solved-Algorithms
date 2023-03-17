from sys import setrecursionlimit
setrecursionlimit(10000)

N, M = tuple(map(int,input().split()))
graph_list = [[] for _ in range(N+1)]
for i in range(M):
    v1, v2 = tuple(map(int,input().split()))
    graph_list[v1].append(v2)
    graph_list[v2].append(v1)
   
 
visited = [False for _ in range(N+1)]

def dfs(now):
    visited[now] = True
    for neig in graph_list[now]:
        if not visited[neig]:
            dfs(neig)
dfs(1)            
comp_conn = [str(idx) for idx, elem in enumerate(visited) if elem]
print(len(comp_conn))
print(' '.join(comp_conn))