class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack():
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        new = Node(value, self.top)
        self.top = new

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            value = self.top.value
            self.top = self.top.next
            return value

    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            return self.top.value

    def isEmpty(self):
        return True if not self.top else False