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
            raise Exception("Stack is empty")
        else:
            node = self.top
            self.top = self.top.next
            node.next = None
            return node.value

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            return self.top.value
            
    def isEmpty(self):
        return self.top == None
