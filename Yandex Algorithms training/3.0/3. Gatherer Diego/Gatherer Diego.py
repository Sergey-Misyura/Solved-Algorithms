# DIego

N = 3
diegos_coll = [100, 1, 50]
K = 3
numbers = [300, 0, 75]
counts = []

sorted_coll = sorted(list(set(diegos_coll)))


def bin_search(num, lst):
    if num > lst[-1]:
        return len(lst)
    elif num <= lst[0]:
        return 0
    else:
        low, high, searched = 0, len(lst) - 1, False
        while (low <= high) and (not searched):

            mid = (high + low) // 2

            if lst[mid] < num:
                if lst[mid + 1] < num:
                    low = mid
                else:
                    searched = True

            else:
                high = mid

        return len(lst[:mid]) + 1


for num in numbers:
    counts.append(bin_search(num, sorted_coll))

print(counts)