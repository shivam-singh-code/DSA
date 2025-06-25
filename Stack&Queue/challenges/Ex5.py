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
   
    def is_empty(self):
        return len(self.stack_list) == 0




def reverse_string(string):
    stack = Stack()
    reverse_string = ''
    for char in string:
        stack.push(char)
   
    while not stack.is_empty():
        reverse_string += stack.pop()
   
    return reverse_string


my_string = 'hello'
print(reverse_string(my_string))
