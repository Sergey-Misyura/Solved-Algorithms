import sys

N = int(input())
M = int(input())
stations = {i: [] for i in range(1, N + 1)}
for line_num in range(M):
    line = list(map(int, input().split()))
    for station in line[1:]:
        stations[station].append(line_num)
st1, st2 = list(map(int, input().split()))

graph_lines = [[] for line in range(M)]
for station, lines in stations.items():
    if len(lines) > 1:
        for line in lines:
            graph_lines[line].extend(lines)
start_lines = stations[st1]
end_lines = stations[st2]

if len(set(start_lines).intersection(end_lines)) > 0:
    print(0)
    sys.exit()

queue = start_lines
idx_queue = 0
distances = [-1 for i in range(M)]
for start_line in start_lines:
    distances[start_line] = 0

while idx_queue < len(queue):
    neighs = graph_lines[queue[idx_queue]]
    for neigh in neighs:
        if distances[neigh] == -1:
            if neigh in end_lines:
                print(distances[queue[idx_queue]] + 1)
                sys.exit()
            distances[neigh] = distances[queue[idx_queue]] + 1
            queue.append(neigh)
    idx_queue += 1
print(-1)