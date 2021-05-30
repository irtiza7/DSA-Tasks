class Stack:
    # Constructor that creates an empty stack (list).
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.myStack = []

    # Check if the stack's limit is reached.
    def isFull(self):
        if len(self.myStack) == self.maxSize:
            return True
        else:
            return False
    
    # Check if the stack is empty or not.
    def isEmpty(self):
        if len(self.myStack) == 0:
            return True
        else:
            return False

    # Push method to insert a value in stack.
    def push(self, value):
        if self.isFull():
            print("Stack Overflown")
        else:
            self.myStack.append(value)

    # Pop method to remove last added value from stack.
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            self.myStack.pop()

    # Peek method to return the last added element in stack.
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.myStack[-1]
    
    # clearStack method deletes all values from a stack
    def clearStack(self):
        self.myStack.clear()


stack = Stack(3)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.peek())

stack.pop()

print(stack.peek())

stack.clearStack()

print(stack.peek())