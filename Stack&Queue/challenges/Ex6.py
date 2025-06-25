class Stack:
    def __init__(self):
        self.stack_list = []


    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])
   
    def push(self, value):
        self.stack_list.append(value)
   
    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()
   
    def is_empty(self):
        return len(self.stack_list) == 0
   
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]


    def size(self):
        return len(self.stack_list)


my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)


def sort_stack(stack):
    addtional_stack = Stack()


    while not stack.is_empty():
        print("Main stack \n")
        stack.print_stack()
        temp = stack.pop()
        print(f"poping from main Stack {temp}\n")
        while not addtional_stack.is_empty() and addtional_stack.peek() > temp:
            print(f"addtional stack top value is greater main stack poping {addtional_stack.peek()}\n")
            stack.push(addtional_stack.pop())
            print("Main stack become\n")
            stack.print_stack()
       
        addtional_stack.push(temp)
        print(f"Addtional stack after push of temp value\n")
        addtional_stack.print_stack()
   
    while not addtional_stack.is_empty():
        stack.push(addtional_stack.pop())
    print("main stack after removing all value form the addtion step in final loop \n")
    stack.print_stack()




print("Stack before sorting in ascending order")
my_stack.print_stack()
sort_stack(my_stack)


print("Stack after sorting in ascending order")
my_stack.print_stack()
