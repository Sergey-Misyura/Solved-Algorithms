N = int(input())
train_1 = list(map(int, input().split()))

stack = []
next_num = 1

for carriage in train_1:
    stack.append(carriage)
   
    while stack!=[] and next_num==stack[-1]:
        stack.pop()
        next_num +=1
       
if stack==[]:
    print('YES')
else:
    print('NO')