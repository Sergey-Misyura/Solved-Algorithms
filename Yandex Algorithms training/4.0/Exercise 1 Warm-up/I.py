seq = input()
bracket_dict = {')':'(', '}':'{', ']':'['}
stack = []
is_right = True

for elem in seq:
    if elem in ('(', '{', '['):
        stack.append(elem)
    else:
        if stack and stack[-1] == bracket_dict[elem]:
            stack.pop()
        else:
            print('no')
            is_right = False
            break
        
if is_right:
    if not stack:
        print('yes')
    else:
        print('no')