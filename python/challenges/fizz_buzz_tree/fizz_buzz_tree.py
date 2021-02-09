from data_structures.tree import tree

def fizz_buzz_tree(tree):
    def traverse(current):
        node = Node(fizz_buzz(current.value))
        if current.left:
            node.left = traverse(current.left)
        if current.right:
            node.right = traverse(current.right)
        return node

    cloned_tree = BinaryTree()
    if tree.root:
        cloned_tree.root = traverse(tree.root)
    return cloned_tree

def fizz_buzz(value):
    if value % 15 == 0:
        return 'FizzBuzz'
    elif value % 3 == 0:
        return 'Fizz'
    elif value % 5 == 0:
        return 'Buzz'
    else:
        return str(value)


##############################

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self) -> list:
        result = []
        def traverse(root):
            result.append(root.value)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        if self.root:
            traverse(self.root)
        return result