from math import ceil

K1, M, K2, P2, N2 = map(int, input().split())
K1, K2 = K1 - 1, K2 - 1

if N2 > M:
    print(-1, -1)
elif P2 == 1 and N2 == 1:
    if K1 <= K2:
        print(1, 1)
    else:
        rooms = K2 + 1
        if K1 < rooms * M:
            print(1, 0)
        else:
            if M == 1:
                print(0, 1)
            else:
                print(0, 0)

else:
    floors = (P2-1) * M + (N2-1)
    max_rooms = K2 // floors
    if max_rooms == 0:
        print(-1, -1)
    else:
        min_rooms = ceil((K2 + 1) / (floors + 1))
        if min_rooms > max_rooms:
            print(-1, -1)
        else:
            up_lim_floors = K1 // min_rooms
            up_lim_P1 = up_lim_floors // M
            up_lim_N1 = up_lim_floors % M

            down_lim_floors = K1 // max_rooms
            down_lim_P1 = down_lim_floors // M
            down_lim_N1 = down_lim_floors % M

            P1 = up_lim_P1 + 1 if up_lim_P1 == down_lim_P1 else 0
            N1 = up_lim_N1 + 1 if M == 1 or up_lim_N1 == down_lim_N1 else 0

            print(P1, N1)






