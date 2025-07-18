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
       
    def dequeue(self):
        if len(self.stack1) <= 0:
            return None
        else:
            return self.stack1.pop()


# Create a new queue
q = Queue()


# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)


# Output the front of the queue
print("Front of the queue:", q.peek())


# Dequeue some values
print("Dequeued value:", q.dequeue())
print("Dequeued value:", q.dequeue())


# Enqueue another value
q.enqueue(4)


# Output the front of the queue again
print("Front of the queue:", q.peek())


# Dequeue all remaining values
print("Dequeued value:", q.dequeue())
print("Dequeued value:", q.dequeue())


# Check if the queue is empty
print("Is the queue empty?", q.is_empty())


# Dequeue from an empty queue and check if it returns None
print("Dequeued value from empty queue:", q.dequeue())
