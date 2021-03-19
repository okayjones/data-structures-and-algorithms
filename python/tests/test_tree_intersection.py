import pytest
from challenges.tree_intersection.tree_intersection import tree_intersection
from data_structures.tree.tree import BinaryTree, Node


def test_tree_intersection(bn1, bn2):
    result = ["100", "160", "125", "175", "200", "350", "500"]
    assert tree_intersection(bn1, bn2) == result


def test_tree_intersection_one_empty(bn1):
    assert tree_intersection(bn1, BinaryTree()) == []


def test_tree_intersection_both_empty():
    assert tree_intersection(BinaryTree(), BinaryTree()) == []


@pytest.fixture
def bn1():
    tree = BinaryTree()
    root = Node("150")
    node_100 = Node("100")
    node_250 = Node("250")
    node_75 = Node("75")
    node_160 = Node("160")
    node_200 = Node("200")
    node_350 = Node("350")
    node_125 = Node("125")
    node_175 = Node("175")
    node_300 = Node("300")
    node_500 = Node("500")

    tree.root = root
    root.left = node_100
    root.right = node_250
    node_100.left = node_75
    node_100.right = node_160
    node_250.left = node_200
    node_250.right = node_350
    node_160.left = node_125
    node_160.right = node_175
    node_350.left = node_300
    node_350.right = node_500

    return tree


@pytest.fixture
def bn2():
    tree = BinaryTree()
    root = Node("42")
    node_100 = Node("100")
    node_600 = Node("600")
    node_15 = Node("15")
    node_160 = Node("160")
    node_200 = Node("200")
    node_350 = Node("350")
    node_125 = Node("125")
    node_175 = Node("175")
    node_4 = Node("4")
    node_500 = Node("500")

    tree.root = root
    root.left = node_100
    root.right = node_600
    node_100.left = node_15
    node_100.right = node_160
    node_600.left = node_200
    node_600.right = node_350
    node_160.left = node_125
    node_160.right = node_175
    node_350.left = node_4
    node_350.right = node_500

    return tree