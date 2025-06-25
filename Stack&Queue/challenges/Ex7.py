class Queue:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []


    def peek(self):
        return self.stack1[-1]
   
    def is_empty(self):
        return len(self.stack1) == 0
   
    def enqueue(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)


print("Front of the queue:", q.peek())
print("Is the queue empty?", q.is_empty())