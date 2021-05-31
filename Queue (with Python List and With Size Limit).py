class Queue:

    def __init__(self, ITEM_LIMIT):
        self.queue = []
        self.ITEM_LIMIT = ITEM_LIMIT
        self.itemCount = 0
    
    def __str__(self):
        return f"Queue: {self.queue}"

    def enqueue(self, item):
        if self.isFull() == True:
            return "Queue is Full"
        else:
            self.queue.append(item)
            self.itemCount += 1
            return "Enqueue Successful"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            self.itemCount -= 1
            return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queue[0]

    def isEmpty(self):
        if self.itemCount == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.itemCount == self.ITEM_LIMIT:
            return True
        else:
            return False

    def clearQueue(self):
        self.queue = []
        self.itemCount =  0
        return "Queue Cleared"

    def getItemCount(self):
        return self.itemCount


myQueue = Queue(4)

print(f"Is Empty? {myQueue.isEmpty()}")
print(f"Dequeue: {myQueue.dequeue()}")

print(f"Item Count: {myQueue.getItemCount()}")

print(f"Enqueue: {myQueue.enqueue(1)}")
print(f"Enqueue: {myQueue.enqueue(2)}")
print(f"Enqueue: {myQueue.enqueue(3)}")

print(f"Item Count: {myQueue.getItemCount()}")

print(myQueue.__str__())

print(f"Enqueue: {myQueue.enqueue(4)}")
print(f"Enqueue: {myQueue.enqueue(5)}")
print(f"Enqueue: {myQueue.enqueue(6)}")

print(f"Item Count: {myQueue.getItemCount()}")

print(f"Is Full? {myQueue.isFull()}")

print(myQueue.__str__())

print(f"Clearing: {myQueue.clearQueue()}")

print(f"Item Count: {myQueue.getItemCount()}")

print(myQueue.__str__())
