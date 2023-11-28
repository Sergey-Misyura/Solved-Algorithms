n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

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
    
if n == 0:
    print(*arr2)
elif m == 0:
    print(*arr1)
else:
    print(*merge(arr1, arr2))