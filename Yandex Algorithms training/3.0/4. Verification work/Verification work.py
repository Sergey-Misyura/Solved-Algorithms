N = int(input())
K = int(input())
row = int(input())
seat = int(input())

result_list = []
taken_seat_num = (row - 1) * 2 + seat

if taken_seat_num - K <= 0 and taken_seat_num + K > N:
    print(-1)

if taken_seat_num - K > 0:
    prev_seat_num = taken_seat_num - K
    prev_row = (prev_seat_num + 1) // 2
    prev_seat = prev_seat_num - (prev_row - 1) * 2
    result_list.append([prev_row, prev_seat])

if taken_seat_num + K <= N:
    after_seat_num = taken_seat_num + K
    after_row = (after_seat_num + 1) // 2
    after_seat = after_seat_num - (after_row - 1) * 2
    result_list.append([after_row, after_seat])

if len(result_list) == 1:
    print(result_list[0][0], result_list[0][1])
elif len(result_list) == 2:
    if row - result_list[0][0] >= result_list[1][0] - row:
        print(result_list[1][0], result_list[1][1])
    else:
        print(result_list[0][0], result_list[0][1])