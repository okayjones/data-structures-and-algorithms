import pytest
from challenges.breadth_first.breadth_first import breadth
from data_structures.tree.tree import BinaryTree, Node

def test_binary_tree_breadth_first_balanced(bn_tree_b):
    actual = breadth(bn_tree_b)
    expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    assert actual == expected

def test_binary_tree_breadth_firt_unbalanced(bn_tree_ub):
    actual = breadth(bn_tree_ub)
    expected = ['A', 'B', 'C', 'D']
    assert actual == expected

def test_binary_tree_breadth_first_empty():
    actual = breadth(BinaryTree())
    expected = []
    assert actual == expected

@pytest.fixture
def bn_tree_b():
    tree = BinaryTree()
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')

    tree.root = a
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    return tree

@pytest.fixture
def bn_tree_ub():
    tree = BinaryTree()
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')

    tree.root = a
    a.left = b
    a.right = c
    b.right = d

    return tree