from math import factorial
from math import gcd

n = int(input())
a = list(map(int, input().split()))

def count_inversion(a):
    total = 0
    size = len(a)
    counts = [0] * size
    rank = {v: i for i, v in enumerate(sorted(a))}
    for u in reversed(a):
        i = rank[u]
        j = i + 1
        while i:
            total += counts[i]
            i -= i & -i
        while j < size:
            counts[j] += 1
            j += j & -j
    return total

start_invers = count_inversion(tuple(a))
total_invers = 0

for i in range(n):
    cur_count = 0
    for j in range(i+1, n):
        if a[j] > a[i]:
            cur_count += 1
        elif a[i] > a[j]:
            cur_count -= 1
        total_invers += start_invers + cur_count

    cur_count = 0
    for j in range(i-1, -1, -1):
        if a[j+1] < a[i]:
            cur_count += 1
        elif a[i] < a[j+1]:
            cur_count -= 1
        total_invers += cur_count

 
vars = int(factorial(n)/(2 * factorial(n - 2)))
gcd_ = gcd(total_invers, vars)
print(f'{int(total_invers/gcd_)}/{int(vars/gcd_)}')

