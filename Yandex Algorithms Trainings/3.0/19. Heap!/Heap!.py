N = int(input())
heap =[]

for _ in range(N):
    command = list(map(int, input().split()))
   
    if command[0]==0:
       
        heap.append(command[1])
        i = len(heap)-1

        while i!=0 and heap[(i-1)//2] < heap[i]:
            heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
            i = (i-1)//2
           
    elif command[0]==1:

        if len(heap)==1:
            print(heap.pop())
        else:
            print(heap[0])
            heap[0] = heap.pop(len(heap)-1)

        i, sift = 0, False
        while (2*i+1 <= len(heap)-1) and not sift:
            if 2*i+2<= len(heap)-1:
                if heap[2*i+1] > heap[i] and heap[2*i+1] > heap[2*i+2]:
                    heap[i], heap[2*i+1] =heap[2*i+1], heap[i]
                    i = 2*i+1
                elif heap[2*i+2] > heap[i] and heap[2*i+2] >= heap[2*i+1]:
                    heap[i], heap[2*i+2] =heap[2*i+2], heap[i]
                    i = 2*i+2
                else:
                    sift = True
            else:
                if heap[2*i+1] > heap[i]:
                    heap[i], heap[2*i+1] =heap[2*i+1], heap[i]
                    i = 2*i+1
                else:
                    sift = True