expr = input().split()
stack = []

for elem in expr:
    if elem.isdigit():
        stack.append(elem)
    else:
        operand_2 = stack.pop()
        res = eval(stack.pop() + elem + operand_2)
        stack.append(str(res))

print(int(stack[0]))