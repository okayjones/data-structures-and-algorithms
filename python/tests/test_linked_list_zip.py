from challenges.ll_zip import __version__
from challenges.ll_zip.ll_zip import zipLists

from data_structures.linked_list.linked_list import LinkedList, Node

def test_version():
    assert __version__ == "0.1.0"

def test_linked_list_zip_same_size():
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(2)
    ll2 = LinkedList()
    ll2.append(5)
    ll2.append(9)
    ll2.append(4)
    expected = LinkedList()
    expected.append(1)
    expected.append(5)
    expected.append(3)
    expected.append(9)
    expected.append(2)     
    expected.append(4)
    actual = zipLists(ll1, ll2) 
    assert str(actual) == str(expected)

def test_linked_list_zip_list1_shorter():
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll2 = LinkedList()
    ll2.append(5)
    ll2.append(9)
    ll2.append(4)
    expected = LinkedList()
    expected.append(1)
    expected.append(5)
    expected.append(3)
    expected.append(9)   
    expected.append(4)
    actual = zipLists(ll1, ll2)
    assert str(actual) == str(expected)

def test_linked_list_zip_list1_longer():
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(2)
    ll2 = LinkedList()
    ll2.append(5)
    ll2.append(9)
    expected = LinkedList()
    expected.append(1)
    expected.append(5)
    expected.append(3)
    expected.append(9)   
    expected.append(2)
    actual = zipLists(ll1, ll2)
    assert str(actual) == str(expected)
    