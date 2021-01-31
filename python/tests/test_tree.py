import pytest
from data_structures.tree import __version__
from data_structures.tree.tree import Node, BinaryTree, BinarySearchTree

def test_version():
    assert __version__ == "0.1.0"

# Can successfully instantiate an empty tree
def test_binary_tree_empty():
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected

# Can successfully instantiate a tree with a single root node
def test_binary_tree_root():
    node = Node('A')
    tree = BinaryTree(node)
    actual = tree.root.value
    expected = node.value
    assert actual == expected

# Can successfully add a left child and right child to a single root node
def test_binary_tree_children():
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    tree = BinaryTree(node_b)
    tree.root.left = node_b
    tree.root.right = node_c
    assert tree.root.left.value == 'B'
    assert tree.root.right.value == 'C'

# Can successfully return a collection from a preorder traversal
def test_binary_tree_pre_order(bn_tree):
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
    actual = bn_tree.pre_order()
    assert actual == expected

# Can successfully return a collection from an inorder traversal
def test_binary_tree_in_order(bn_tree):
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
    actual = bn_tree.in_order()
    assert actual == expected

# Can successfully return a collection from a postorder traversal
def test_binary_tree_post_order(bn_tree):
    expected = ['D', 'E', 'B', 'F', 'C', 'A']
    actual = bn_tree.post_order()
    assert actual == expected

# BST - Can add node to empty tree
def test_binary_search_tree_add_empty():
    value = 5
    tree = BinarySearchTree()
    tree.add(value)
    actual = tree.root.value
    expected = value
    assert actual == expected
    assert tree.root.left == None
    assert tree.root.left == None

# BST - can add node to tree right
def test_binary_search_tree_add_right(bst_tree):
    bst_tree.add(85)
    actual = bst_tree.pre_order()
    expected = [23, 8, 4, 16, 42, 27, 85]
    assert actual == expected

# BST - can add node to tree left
def test_binary_search_tree_add_left(bst_tree):
    bst_tree.add(15)
    actual = bst_tree.pre_order()
    expected = [23, 8, 4, 16, 15, 42, 27]
    assert actual == expected

# BST - Can search for existing value in tree
def test_binart_search_tree_contains_true(bst_tree):
    actual = bst_tree.contains(16)
    expected = True
    assert actual == expected

# BST - Can search for missing value in tree
def test_binart_search_tree_contains_false(bst_tree):
    actual = bst_tree.contains(15)
    expected = False
    assert actual == expected

@pytest.fixture
def bn_tree():
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

@pytest.fixture
def bst_tree():
    tree = BinarySearchTree()
    a = Node(23)
    b = Node(8)
    c = Node(42)
    d = Node(4)
    e = Node(16)
    f = Node(27)

    tree.root = a
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f

    return tree
    