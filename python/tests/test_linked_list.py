from data_structures.linked_list import __version__
from data_structures.linked_list.linked_list import LinkedList, Node


def test_version():
    assert __version__ == '0.1.0'

def test_linked_list_empty():
    ll = LinkedList()
    actual = ll.head
    expected = None
    assert actual == expected

def test_linked_list_insert():
    value = 10
    ll = LinkedList()
    ll.insert(value)
    actual = ll.head.value
    expected = value
    assert actual == expected 