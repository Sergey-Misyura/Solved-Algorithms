p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))

move = 0

while len(p1)!=0 and len(p2)!=0 and move < 10**6:

    move+=1
    p1_card, p2_card, p1_win, p2_win, draw = p1.pop(0), p2.pop(0), False, False, False

    if (p1_card, p2_card) == (0, 9):
        p1_win = True
    elif (p1_card, p2_card) == (9, 0):
        p2_win = True
    elif p1_card > p2_card:
        p1_win = True
    elif p2_card > p1_card:
        p2_win = True
    else:
        draw = True

    if p1_win:
        p1.append(p1_card)
        p1.append(p2_card)
    elif p2_win:
        p2.append(p1_card)
        p2.append(p2_card)
    elif draw:
        p1.append(p1_card)
        p2.append(p2_card)

if len(p1)==0:
    print(f'second {move}')
elif len(p2)==0:
    print(f'first {move}')
else:
    print('botva')