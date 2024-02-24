class Stack():
   
    def __init__(self):
        self.stack = []
       
    def push(self, item):
        self.stack.append(item)
        return 'ok'
   
    def pop(self):
        return self.stack.pop() if self.size()!=0 else 'error'
         
    def back(self):
        return self.stack[-1] if self.size()!=0 else 'error'
   
    def size(self):
        return len(self.stack)
       
    def clear(self):
        self.stack = []
        return 'ok'
   
    def exit(self):
        return 'bye'

command = [[]]
stack = Stack()

while command[0]!='exit':
    command = input().split()
   
    if command[0]=='push':
        print(eval(f'stack.push({command[1]})'))
    else:
        print(eval('stack.'+command[0]+'()'))