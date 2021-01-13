import pytest
from data_structures.stacks_and_queues.stacks_and_queues import Node, Stack, Queue
from data_structures.stacks_and_queues import __version__

def test_version():
    assert __version__ == "0.1.0"

# STACKS
# Can successfully push onto a stack
def test_stack_push_one():
    value = 1
    stack = Stack()
    stack.push(value)
    actual = stack.top.value
    expected = value
    assert actual == expected

# Can successfully push multiple values onto a stack
def test_stack_push_many():
    value1 = 1
    value2 = 2
    stack = Stack()
    stack.push(value1)
    stack.push(value2)
    actual = stack.top.value
    expected = value2
    assert actual == expected

# Can successfully pop off the stack
def test_stack_pop():
    value1 = 1
    value2 = 2
    stack = Stack()
    stack.push(value1)
    stack.push(value2)
    actual = stack.pop()
    expected = value2
    assert actual == expected

# Can successfully empty a stack after multiple pops
def test_stack_pop_until_empty():
    value1 = 1
    value2 = 2
    stack = Stack()
    stack.push(value1)
    stack.push(value2)
    stack.pop()
    stack.pop()
    actual = stack.top
    expected = None
    assert actual == expected

# Can successfully peek the next item on the stack
def test_stack_peek():
    value = 1
    node = Node(value)
    stack = Stack(node)
    actual = stack.peek()
    expected = value
    assert actual == expected
    
# Can successfully instantiate an empty stack
def test_stack_new_empty():
    stack = Stack()
    actual = stack.top
    expected = None
    assert actual == expected

# Calling pop or peek on empty stack raises exception
def test_stack_pop_empty_exception():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()

def test_stack_peek_empty_exception():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()

# QUEUES
# Can successfully enqueue into a queue
def test_queue_enqueue():
    value = 1
    queue = Queue()
    queue.enqueue(value)
    expected = value
    actual = queue.front.value
    assert actual == expected

# Can successfully enqueue multiple values into a queue
def test_queue_enqueue_many():
    value1 = 1
    value2 = 2
    queue = Queue()
    queue.enqueue(value1)
    queue.enqueue(value2)
    expected = value1
    actual = queue.front.value
    assert actual == expected
    
# Can successfully dequeue out of a queue the expected value
def test_queue_dequeue():
    value = 1
    queue = Queue()
    queue.enqueue(value)
    actual = queue.dequeue()
    expected = value
    assert actual == expected

# Can successfully peek into a queue, seeing the expected value
def test_queue_peek():
    value = 1
    node = Node(value)
    queue = Queue(node)
    actual = queue.peek()
    expected = value
    assert actual == expected

# Can successfully empty a queue after multiple dequeues
def test_queue_dequeue_until_empty():
    value1 = 1
    value2 = 2
    queue = Queue()
    queue.enqueue(value1)
    queue.enqueue(value2)
    queue.dequeue()
    queue.dequeue()
    actual = queue.front
    expected = None
    assert actual == expected

# Can successfully instantiate an empty queue
def test_queue_new_empty():
    queue = Queue()
    actual = queue.front
    expected = None
    assert actual == expected

# Calling dequeue or peek on empty queue raises exception
def test_queue_dequeue_empty_exception():
    queue = Queue()
    with pytest.raises(Exception):
        queue.dequeue()

def test_queue_peek_empty_exception():
    queue = Queue()
    with pytest.raises(Exception):
        queue.peek()