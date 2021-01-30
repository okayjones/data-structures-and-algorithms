from data_structures.tree import __version__

def test_version():
    assert __version__ == "0.1.0"


# Can successfully instantiate an empty tree
# Can successfully instantiate a tree with a single root node
# Can successfully add a left child and right child to a single root node
# Can successfully return a collection from a preorder traversal
# Can successfully return a collection from an inorder traversal
# Can successfully return a collection from a postorder traversal