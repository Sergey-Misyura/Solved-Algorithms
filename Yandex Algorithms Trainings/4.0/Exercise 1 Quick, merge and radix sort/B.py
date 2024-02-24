from random import randint

n = int(input())
arr = list(map(int, input().split()))

def partition(l, r, x):
    E = G = -1
    
    for idx in range(l, r+1):
        
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
    
def quicksort(l, r):
    x = arr[randint(l,r)]
    E, G = partition(l, r, x)
    if E - l > 0:
        quicksort(l, E-1)
    if G > -1:
        quicksort(G,r)
    
if n == 0:
    print ('')
else:
    quicksort(0, len(arr)-1)        
    print(*arr)
