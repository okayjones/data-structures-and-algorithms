class PseudoQueue():
    def __init__(self):
        """Constructor for PseudoQueue class, implemented using two Stacks. 
        """
        self.input =  Stack()
        self.output = Stack()

    def enqueue(self, value):
        """Enqueue adds to the queue. 

        Args:
            value (any): A value to add to the queue.
        """
        self.input.push(value)

    def dequeue(self):
        """Dequeue removes and returns a value from the queue in FIFO order.

        Returns:
            value: Value being removed from the queue
        """
        
        #Empty input stack into output stack
        while True:
            try:
                value = self.input.pop()
                self.output.push(value)
            except Exception: 
                break
       
        #Return top of output stack, or None if empty
        try:
            return self.output.pop()
        except Exception:
            return None


#### FIGURE OUT HOW TO IMPORT THIS INSTEAD ####
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