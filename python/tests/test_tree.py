import pytest
from data_structures.tree import __version__
from data_structures.tree.tree import Node, BinaryTree, BinarySearchTree

def test_version():
    assert __version__ == "0.1.0"


# Can successfully instantiate an empty tree
# Can successfully instantiate a tree with a single root node
# Can successfully add a left child and right child to a single root node


# Can successfully return a collection from a preorder traversal
def test_binary_tree_pre_order(test_tree):
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
    actual = test_tree.pre_order()
    assert actual == expected

# Can successfully return a collection from an inorder traversal
def test_binary_tree_in_order(test_tree):
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
    actual = test_tree.in_order()
    assert actual == expected

# Can successfully return a collection from a postorder traversal
def test_binary_tree_post_order(test_tree):
    expected = ['D', 'E', 'B', 'F', 'C', 'A']
    actual = test_tree.post_order()
    assert actual == expected


@pytest.fixture
def test_tree():
    tree = BinaryTree()
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')

    tree.root = a
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f

    return tree