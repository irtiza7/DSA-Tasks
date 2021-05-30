class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def insertNode(self, value):
        if self.isEmpty():
            self.head = Node(value)
        else:
            current = self.head
            node = Node(value)
            node.next_node = current
            self.head = node

    def deleteNode(self):
        if self.isEmpty():
            print("Empty")
        else:
            self.head = self.head.next_node
    
    def clearLinkedList(self):
        self.head = None
    
    def displayLinkedList(self):
        if self.isEmpty():
            print("Empty")
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next_node

    def getHead(self):
        return self.head.value


class Stack(SingleLinkedList):
    def __init__(self):
        super().__init__()

    def isEmpty(self):
        super().isEmpty()
    
    def push(self, value):
        super().insertNode(value)
    
    def pop(self):
        self.poppedNode = super().getHead()
        super().deleteNode()
        return self.poppedNode

    def peek(self):
        return super().getHead()
    
    def clearStack(self):
        super().clearLinkedList()

    def displayStack(self):
        super().displayLinkedList()


stack = Stack()

print("Pushing 5 values")
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("Current Stack Contents....")
stack.displayStack()

print("Pushing 1 value")
stack.push(6)

print("Current Stack Contents....")
stack.displayStack()

print("Popping 1 value")
stack.pop()

print("Current Stack Contents....")
stack.displayStack()

print("Pushing 1 value")
stack.push(7)
stack.displayStack()

print("Clearing Stack")
stack.clearStack()

print("Current Stack Contents....")
stack.displayStack()