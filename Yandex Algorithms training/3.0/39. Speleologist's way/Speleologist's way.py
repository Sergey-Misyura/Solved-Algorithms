import sys

N = int(input())
cave = []
coord_start = ()
for level_num in range(N):
    cave_level = []
    delimiter = input()
    for line_num in range(N):
        line = input()
        cave_line = [0 if i == "#" else 1 for i in line]
        if "S" in line:
            coord_start = (level_num, line_num, line.find("S"))
        cave_level.append(cave_line)
    cave.append(cave_level)

if coord_start[0] == 0:
    print(0)
    sys.exit(0)

distances = [[[-1 for block in range(N)] for line in range(N)] for level in range(N)]

k, i, j = coord_start
distances[k][i][j] = 0
queue = [tuple(coord_start)]
idx_queue = 0

while True:
   
    neigh_blocks = []
    curr_coords = queue[idx_queue]
    for shift in (1, -1):
        for idx_coord in (0, 1, 2):
            neigh = list(curr_coords)
            neigh[idx_coord] += shift
            k, i, j = neigh
            if N>k>=0 and N>i>=0 and N>j>=0:
                if distances[k][i][j]==-1 and cave[k][i][j]==1:
                    if k==0:
                        print(distances[curr_coords[0]][curr_coords[1]][curr_coords[2]]+1)
                        sys.exit()
                    neigh_blocks.append(neigh)
   
    for block in neigh_blocks:
        k, i, j = block
        distances[k][i][j] = distances[curr_coords[0]][curr_coords[1]][curr_coords[2]]+1
        queue.append(block)
       
    idx_queue+=1