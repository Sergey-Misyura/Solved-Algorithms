from sys import setrecursionlimit
setrecursionlimit(100000)

N, M = tuple(map(int,input().split()))
graph_list = [[] for _ in range(N+1)]
for i in range(M):
    v1, v2 = tuple(map(int,input().split()))
    graph_list[v1].append(v2)
    graph_list[v2].append(v1)
   
 
visited = [False for _ in range(N+1)]

def dfs(now):
    visited[now] = True
    comp_list[comp].append(now)
    for neig in graph_list[now]:
        if not visited[neig]:
            dfs(neig)
comp = 0
comp_list = [[]]
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        comp_list.append([])
        comp+=1
comp_list.pop()

print(len(comp_list))
for lst in comp_list:
    print(len(lst))
    print(' '.join([str(el) for el in lst]))