import pytest
from data_structures.stacks_and_queues.stacks_and_queues import Node, Stack
from data_structures.stacks_and_queues import __version__

def test_version():
    assert __version__ == "0.1.0"


## STACKS
# Can successfully push onto a stack
# Can successfully push multiple values onto a stack
# Can successfully pop off the stack
# Can successfully empty a stack after multiple pops
# Can successfully peek the next item on the stack
# Can successfully instantiate an empty stack
# Calling pop or peek on empty stack raises exception
def test_pop_empty_stack_exception():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()

## QUEUES
# Can successfully enqueue into a queue
# Can successfully enqueue multiple values into a queue
# Can successfully dequeue out of a queue the expected value
# Can successfully peek into a queue, seeing the expected value
# Can successfully empty a queue after multiple dequeues
# Can successfully instantiate an empty queue
# Calling dequeue or peek on empty queue raises exception