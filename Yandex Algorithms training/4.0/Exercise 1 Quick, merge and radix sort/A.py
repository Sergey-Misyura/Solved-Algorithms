n = int(input())
arr = list(map(int, input().split()))
x = int(input())

def partition(a, b, x):
    E = G = -1
    
    for idx in range(a, b+1):
        
        if arr[idx] > x:
            if G == -1:
                G = idx
        elif arr[idx] == x:
            if G > -1:
                if E == -1:
                    E = G
                arr[G], arr[idx] = arr[idx], arr[G]
                G +=1    
            elif E == -1 and G == -1:
                E = idx
                
        elif arr[idx] < x:
            if E > -1 and G > -1:
                arr[E], arr[G], arr[idx] = arr[idx], arr[E], arr[G]
                E +=1 
                G +=1
            elif G > -1:
                arr[G], arr[idx] = arr[idx], arr[G]
                G +=1
            elif E > -1:
                arr[E], arr[idx] = arr[idx], arr[E]
                E +=1
    return E, G
    
    
if n == 0:
    print(0, 0, sep='\n')
else:
    E, G = partition(0, len(arr)-1, x)
    if E == -1 and G == -1:
        print(len(arr), 0, sep='\n')
    elif E > -1:
        print(E, len(arr)-E, sep='\n')
    else:
        print(G, len(arr)-G, sep='\n')
