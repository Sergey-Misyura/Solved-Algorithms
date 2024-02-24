import sys

N, M, S, T, Q = list(map(int, input().split()))
fleas = []
for _ in range(Q):
    fleas.append(tuple(map(int, input().split())))

distances = [[-1 for _ in range(M+1)] for i in range(N+1)]
distances[S][T] = 0
queue, idx_queue = [(S,T)], 0

dx = (1, 2, 2, 1, -1, -2, -2, -1)
dy = (2, 1, -1, -2, -2, -1, 1, 2)
while idx_queue < len(queue):
    curr_x, curr_y = queue[idx_queue]
   
    for i in range(8):
        next_x, next_y = curr_x+dx[i], curr_y+dy[i]
        if N>=next_x>0 and M>=next_y>0 and distances[next_x][next_y]==-1:
            distances[next_x][next_y] = distances[curr_x][curr_y]+1
            queue.append((next_x, next_y))
           
    idx_queue+=1

total = 0
for flea in fleas:
    if distances[flea[0]][flea[1]]==-1:
        print(-1)
        sys.exit()
    total+=distances[flea[0]][flea[1]]
   
print(total)