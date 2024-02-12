N = int(input().strip())
top = 4000.0
bot = 30.0

cur = float(input().strip())
for _ in range(N - 1):
    new, dist = input().split()
    new = float(new)
    median = (cur + new) / 2

    if new < cur:
        if dist == 'closer' and top > median:
            top = median
        elif dist == 'further' and bot < median:
            bot = median

    elif new > cur:
        if dist == 'closer' and bot < median:
            bot = median
        elif dist == 'further' and top > median:
            top = median

    cur = new


print(bot, top)

