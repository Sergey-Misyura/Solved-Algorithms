n, m = map(int, input().split())
arr = list(map(int, input().split()))
res_dict = {}

for _ in range(m):
	l, r = map(int, input().split())
	arr_min = arr[l]
	for i in range (l, r+1):
	    if arr[i] > arr_min:
	        print(arr[i])
	        break
	    elif arr[i] < arr_min:
	        print(arr_min)
	        break
	else:
	    print('NOT FOUND')     