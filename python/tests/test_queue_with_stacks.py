from challenges.queue_with_stacks.queue_with_stacks import PseudoQueue
from challenges.queue_with_stacks import __version__

def test_version():
    assert __version__ == "0.1.0"

def test_pseudoqueue_enqueue_one():
    value = 1
    queue = PseudoQueue()
    queue.enqueue(value)
    actual = queue.input.peek()
    expected = value
    assert actual == expected

def test_pseudoqueue_enqueue_many():
    value1 = 1
    value2 = 2
    queue = PseudoQueue()
    queue.enqueue(value1)
    queue.enqueue(value2)
    actual = queue.input.peek()
    expected = value2
    assert actual == expected

def test_pseudoqueue_dequeue_one():
    value = 1
    queue = PseudoQueue()
    queue.enqueue(value)
    actual = queue.dequeue()
    expected = value
    assert actual == expected

def test_pseudoqueue_dequeue_many():
    value1 = 1
    value2 = 2
    queue = PseudoQueue()
    queue.enqueue(value1)
    queue.enqueue(value2)
    queue.dequeue()
    actual = queue.dequeue()
    expected = value2
    assert actual == expected

def test_pseudoqueue_dequeue_empty():
    value1 = 1
    value2 = 2
    queue = PseudoQueue()
    queue.enqueue(value1)
    queue.enqueue(value2)
    queue.dequeue()
    queue.dequeue()
    actual = queue.dequeue()
    expected = None
    assert actual == expected