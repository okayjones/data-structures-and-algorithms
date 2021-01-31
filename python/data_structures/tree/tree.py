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
    def add(self, value):
        if not self.root:
            self.root = Node(value)

        def add_helper(root):
            if value < root.value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    add_helper(root.left)
            elif value > root.value:
                if root.right is None:
                    root.right = Node(value)
                else:
                    add_helper(root.right)
        add_helper(self.root)

    def contains(self, value):
        root = self.root
        while root:
            if root.value == value:
                return True
            elif value < root.value:
                root = root.left
            elif value > root.value:
                root = root.right
        return False
