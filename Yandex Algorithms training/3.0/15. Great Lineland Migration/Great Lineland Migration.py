N=int(input())
a = list(map(int, input().split()))

output, stack = ['-1' for _ in range(len(a))], []

for idx, price in enumerate(a):
   
    while len(stack)!=0 and stack[-1][0] > price:
        pop_price = stack.pop()
        output[pop_price[1]] = str(idx)
       
    stack.append((price, idx))

print(' '.join(output))