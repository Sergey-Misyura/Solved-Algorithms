N = int(input())
graph_matrix = []
for _ in range(N):
    graph_matrix.append(list(map(int, input().split())))

vert1, vert2 = tuple(map(int, input().split()))
vert1 -=1
vert2 -=1

distances = [-1 for _ in range(N)]
distances[vert1] = 0
queue = [vert1]
queue_idx = 0

while distances[vert2] == -1 and queue_idx < len(queue):
    prev = queue[queue_idx]
    for vert, edge in enumerate(graph_matrix[prev]):
        if edge==1 and distances[vert]==-1:
            queue.append(vert)
            distances[vert] = distances[prev]+1
    queue_idx +=1

print(distances[vert2])