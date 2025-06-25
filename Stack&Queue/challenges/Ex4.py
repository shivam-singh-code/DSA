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
       


def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push('(')
        elif p == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()


print(is_balanced_parentheses('((()))'))
print(is_balanced_parentheses('((())))'))
