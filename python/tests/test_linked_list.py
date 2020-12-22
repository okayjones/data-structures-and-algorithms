from data_structures.linked_list import __version__
from data_structures.linked_list.linked_list import LinkedList, Node


def test_version():
    assert __version__ == '0.1.0'

def test_linked_list_empty():
    ll = LinkedList()
    actual = ll.head
    expected = None
    assert actual == expected

def test_linked_list_head():
    value = 10
    node = Node(10)
    ll = LinkedList(node)
    actual = ll.head
    expected = node
    assert actual == expected

def test_linked_list_insert():
    value = 10
    ll = LinkedList()
    ll.insert(value)
    actual = ll.head.value
    expected = value
    assert actual == expected

def test_linked_list_insert_multiple():
    value1 = 'Monday'
    value2 = 'Tuesday'
    value3 = 'Wednesday'
    ll = LinkedList(Node(value1))
    ll.insert(value2)
    ll.insert(value3)
    actual = ll.head.value
    expected = value3
    assert actual == expected

def test_linked_list_includes_false():
    value = 10
    other_value = 11
    node = Node(10)
    ll = LinkedList(node)
    actual = ll.includes(other_value)
    expected = False
    assert actual == expected

def test_linked_list_includes_true():
    value = 10
    node = Node(10)
    ll = LinkedList(node)
    actual = ll.includes(value)
    expected = True
    assert actual == expected

def test_linked_list_str():
    ll = LinkedList()
    ll.insert('c')
    ll.insert('b')
    ll.insert('a')
    actual = str(ll)
    expected = "{ a } -> { b } -> { c } -> NULL"
    assert actual == expected