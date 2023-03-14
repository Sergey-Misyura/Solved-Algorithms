N = int(input())
diegos_coll = list(map(int, input().split()))
K = int(input())
numbers = list(map(int, input().split()))

sorted_coll = sorted(list(set(diegos_coll)))
coll_len = len(sorted_coll)
searched_dict = {}

for i in range(K):
    num = numbers[i]

    if num <= sorted_coll[0]:
        print(0)
    elif num > sorted_coll[-1]:
        print(coll_len)
    elif num in searched_dict:
        print(searched_dict[num])
    else:

        left, right = 0, len(sorted_coll) - 1

        while left < right:
            mid = (left + right) // 2
            if num > sorted_coll[mid]:
                left = mid + 1
            else:
                right = mid
        searched_dict[num] = left

        print(left)