class Stack:
    def __init__(self):
        self.stack_list = []


    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])
   
    def push(self, value):
        self.stack_list.append(value)
   
    def pop(self):
        if len(self.stack_list) < 0:
            return None
        return self.stack_list.pop()


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.print_stack()


print('Poping element from the stack')
print(my_stack.pop())
print("Stack after Pop")
my_stack.print_stack()
