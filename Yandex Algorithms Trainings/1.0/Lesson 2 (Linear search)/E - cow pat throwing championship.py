from collections import Counter

n = int(input().strip())
dists = list(map(int, input().split()))
top = max(dists)
count = Counter(dists)

prev_top = False
best_dist = float('-inf')
for i in range(n - 1):
    if not prev_top:
        if dists[i] == top:
            prev_top = True
    else:
        if dists[i] % 10 == 5 and dists[i] > dists[i + 1]:
            best_dist = max(best_dist, dists[i])

place = 0

for key, value in sorted(count.items(), reverse=True):
    if key != best_dist:
        place += value
    else:
        place += 1
        break


if best_dist == float('-inf'):
    print(0)
else:
    print(place)

