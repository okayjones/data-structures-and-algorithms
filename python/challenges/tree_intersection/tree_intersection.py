from data_structures.tree.tree import BinaryTree
from data_structures.hashtable.hashtable import Hashtable


def tree_intersection(bn1, bn2):
    ht = Hashtable()
    for n in bn1.pre_order():
        ht.add(n, n)
    return [n for n in bn2.pre_order() if ht.contains(n)]