class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack():
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        node = Node(value, self.top)
        self.top = node

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            node = self.top
            self.top = self.top.next
            node.next = None
            return node.value

    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            return self.top.value

    def isEmpty(self):
        return self.top == None

class Queue():
    def __init__(self, front=None):
        self.front = front
        self.rear = None

    def enqueue(self, value):
        node = Node(value)

        if self.isEmpty():
            self.front = node
            self.rear = node
        else:    
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            return self.front.value

    def isEmpty(self):
        return self.front == None