from stack import Stack

class PseudoQueue():
    def __init__(self):
        self.input =  Stack()
        self.output = Stack()

    def enqueue(self, value):
        self.input.push(value)

    def dequeue(self):
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