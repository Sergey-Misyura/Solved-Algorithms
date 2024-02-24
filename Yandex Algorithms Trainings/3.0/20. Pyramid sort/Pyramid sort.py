N = int(input())
arr = list(map(int, input().split()))
sorted_count = 0

heap_last = len(arr)-1 - sorted_count
last_sort = (heap_last-1)//2

while heap_last!= 0:
# build heap of maximum
    for idx_sort in range(last_sort,-1, -1):
        i, sift = idx_sort, False
   
        while (2*i+1 <= heap_last) and not sift:
            if 2*i+2<= heap_last:
                if arr[2*i+1] > arr[i] and arr[2*i+1] > arr[2*i+2]:
                    arr[i], arr[2*i+1] =arr[2*i+1], arr[i]
                    i = 2*i+1
                elif arr[2*i+2] > arr[i] and arr[2*i+2] >= arr[2*i+1]:
                    arr[i], arr[2*i+2] =arr[2*i+2], arr[i]
                    i = 2*i+2
                else:
                    sift = True
            else:
                if arr[2*i+1] > arr[i]:
                    arr[i], arr[2*i+1] =arr[2*i+1], arr[i]
                    i = 2*i+1
                else:
                    sift = True


    # pop maximum item
    arr[0], arr[heap_last] = arr[heap_last], arr[0]
    sorted_count, heap_last =sorted_count + 1, heap_last-1
    last_sort = 0


print(' '.join(str(x) for x in arr))