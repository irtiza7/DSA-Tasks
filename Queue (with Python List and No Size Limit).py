class Queue:
    def __init__(self):
        self.queue = []
    
    def __str__(self):
        return f"Queue: {self.queue}"

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queue[0]

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def clearQueue(self):
        self.queue = []

myQueue = Queue()

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)

print(myQueue.__str__())

print(f"Dequeued: {myQueue.dequeue()}")

myQueue.enqueue(10)
myQueue.enqueue(20)

print(myQueue.__str__())

print(f"Peek Queue: {myQueue.peek()}")

print(myQueue.__str__())

myQueue.clearQueue()

print(myQueue.__str__())