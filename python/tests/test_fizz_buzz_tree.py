import pytest
from challenges.fizz_buzz_tree.fizz_buzz_tree import fizz_buzz_tree
from challenges.fizz_buzz_tree.fizz_buzz_tree import Node, BinaryTree


def test_fizz_buzz(tree, fb_tree):
    fizzed_tree = fizz_buzz_tree(tree)
    actual = fizzed_tree.pre_order()
    expected = fb_tree.pre_order()
    assert actual == expected


def test_fizz_buzz_empty():
    actual = fizz_buzz_tree(BinaryTree()).pre_order()
    expected = []
    assert actual == expected


def test_fizz_buzz_one():
    root = Node(15)
    actual = fizz_buzz_tree(BinaryTree(root)).pre_order()
    expected = ['FizzBuzz']
    assert actual == expected


@pytest.fixture
def tree():
    tree = BinaryTree()
    a = Node(30)
    b = Node(10)
    c = Node(7)
    d = Node(3)
    e = Node(11)
    f = Node(21)

    tree.root = a
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f

    return tree

@pytest.fixture
def fb_tree():
    tree = BinaryTree()
    a = Node('FizzBuzz')
    b = Node('Buzz')
    c = Node('7')
    d = Node('Fizz')
    e = Node('11')
    f = Node('Fizz')

    tree.root = a
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f

    return tree