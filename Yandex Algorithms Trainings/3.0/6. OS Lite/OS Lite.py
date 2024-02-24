M=int(input())
N=int(input())
if N == 0:
    print (0)
else:
    os_set = set()
    os_set.add(tuple(map(int, input().split())))
   
    if N > 1:
        for i in range(N-1):
            new_os = tuple(map(int, input().split()))
           
            new_set=os_set.copy()
            for os in os_set:
                if new_os[0] <= os[1] and os[0] <= new_os[1]:
                    new_set.remove(os)
                   
            os_set = new_set.copy()      
            os_set.add(new_os)
   
    print(len(os_set))