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
        traverse(self.root)
        return result

    def in_order(self) -> list:
        result = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            result.append(root.value)
            if root.right:
                traverse(root.right)
        traverse(self.root)
        return result

    def post_order(self) -> list:
        result = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            result.append(root.value)
        traverse(self.root)
        return result

class BinarySearchTree(BinaryTree):
    def add():
        pass
    
    def contains():
        pass
