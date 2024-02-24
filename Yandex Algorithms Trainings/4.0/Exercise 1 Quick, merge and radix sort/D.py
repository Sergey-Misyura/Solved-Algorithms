n = int(input())
arr = list(map(int, input().split()))


def merge(arr1, arr2):
    ans_arr = [0] * (len(arr1)+len(arr2))
    idx1 = idx2 = 0
    for idx_ans in range(len(ans_arr)):
        if idx1 < len(arr1) and idx2 < len(arr2):
            if arr1[idx1] <= arr2[idx2]:
                ans_arr[idx_ans] = arr1[idx1]
                idx1 +=1
            else:
                ans_arr[idx_ans] = arr2[idx2]
                idx2 +=1
        elif idx1 == len(arr1):
            ans_arr[idx_ans] = arr2[idx2]
            idx2 +=1
        elif idx2 == len(arr2):
            ans_arr[idx_ans] = arr1[idx1]
            idx1 +=1
    
    return ans_arr


def mergesort(l, r):

    if l == r:
        return [arr[l]]
    
    arr1 = mergesort(l, (l+r)//2)
    arr2 = mergesort((l+r)//2+1, r)
    
    return merge(arr1, arr2)
    

if n == 0:
    print('')
else:
    print(*mergesort(0, len(arr)-1)) 