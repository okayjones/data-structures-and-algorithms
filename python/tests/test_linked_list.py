import pytest
from data_structures.linked_list.linked_list import LinkedList, Node

# Code Challenge 05
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

#Code Challenge 06
def test_linked_list_append():
    ll = LinkedList()
    ll.insert('c')
    ll.insert('b')
    ll.insert('a')
    ll.append('d')
    actual = str(ll)
    expected = "{ a } -> { b } -> { c } -> { d } -> NULL"
    assert actual == expected

def test_linked_list_append_multiple():
    ll = LinkedList()
    ll.insert('c')
    ll.insert('b')
    ll.insert('a')
    ll.append('d')
    ll.append('e')
    actual = str(ll)
    expected = "{ a } -> { b } -> { c } -> { d } -> { e } -> NULL"
    assert actual == expected

def test_linked_list_insert_before_middle():
    ll = LinkedList()
    ll.append('a')
    ll.append('c')
    ll.insertBefore('c', 'b')
    actual = str(ll)
    expected = "{ a } -> { b } -> { c } -> NULL"
    assert actual == expected

def test_linked_list_insert_before_first():
    ll = LinkedList()
    ll.append('b')
    ll.append('c')
    ll.insertBefore('b', 'a')
    actual = str(ll)
    expected = "{ a } -> { b } -> { c } -> NULL"
    assert actual == expected

def test_linked_list_insert_after_middle():
    ll = LinkedList()
    ll.append('a')
    ll.append('c')
    ll.insertAfter('a', 'b')
    actual = str(ll)
    expected = "{ a } -> { b } -> { c } -> NULL"
    assert actual == expected

def test_linked_list_insert_after_end():
    ll = LinkedList()
    ll.append('a')
    ll.append('b')
    ll.insertAfter('b', 'c')
    actual = str(ll)
    expected = "{ a } -> { b } -> { c } -> NULL"
    assert actual == expected

# Code Challenge 07
def test_linked_list_kth_greater_than():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    with pytest.raises(Exception):
        ll.kthFromEnd(6)

def test_linked_list_kth_equal_length():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    with pytest.raises(Exception):
        ll.kthFromEnd(4)

def test_linked_list_kth_negative_int():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    with pytest.raises(Exception):
        ll.kthFromEnd(-4)

def test_linked_list_kth_size_one_fail():
    ll = LinkedList()
    ll.append(1)
    with pytest.raises(Exception):
        ll.kthFromEnd(1)

def test_linked_list_kth_size_one_pass():
    ll = LinkedList()
    ll.append(1)
    actual = ll.kthFromEnd(0)
    expected = 1
    assert actual == expected

def test_linked_list_kth_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    actual = ll.kthFromEnd(2)
    expected = 3
    assert actual == expected