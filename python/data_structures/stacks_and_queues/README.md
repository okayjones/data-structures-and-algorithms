# Stacks and Queues

Python implementation of a Stack and Queue

## Challenge

Create a Stack and Queue class with basic methods. Both classes should use a Node class with a next pointer for their implementations.

## Approach & Efficiency

Both Stack and Queue classes were implemented using the Node class. All methods are O(n) as the size of the stack and queue are not relevant.

## API

### Stack

- `.push(value)` - Add a new value to the top of the stack
- `.pop()` -  Removes the value on the top of the stack
- `.peek()` - Return the value at the top of the stack
- `.isEmpty()` - Returns True if the stack is empty, False otherwise

### Queue

- `.enqueue(value)` - Add a new value to the end of the queue
- `.dequeue()` - Removes value from the front of the queue
- `.peek()` - Return the value at the front of the queue
- `.isEmpty()` - Returns True if the queue is empty, False otherwise
