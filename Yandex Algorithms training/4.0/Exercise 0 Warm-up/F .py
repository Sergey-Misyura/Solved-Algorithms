reader = open('input.txt', 'r')

max_count = int(reader.readline())
floors_count = int(reader.readline())
floors = [0] + [0] * floors_count
for i in range(1, floors_count + 1):
    floors[i] = int(reader.readline())
reader.close()

i = floors_count
total_time = 0

while i != 0:
    if floors[i] != 0:
        times, ret = divmod(floors[i], max_count)
        total_time += times * 2 * i
        if ret == 0:
            i -= 1
        else:
            ret = max_count - ret
            total_time += 2 * i
            while ret > 0 and i > 0:
                i -= 1
                cur_min = min(floors[i], ret)
                ret -= cur_min
                floors[i] -= cur_min
    else:
        i -=1

print(total_time)