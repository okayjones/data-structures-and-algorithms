class Node:
    """Simple Node class for a binary tree
    """
    def __init__(self, value, left=None, right=None):
        """Node constructor

        Args:
            value (any): value to assign to the node
            left (Node, optional): Left node. Defaults to None.
            right (Node, optional): Right node. Defaults to None.
        """
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    """Binary tree class
    """
    def __init__(self, root=None):
        """Binary tree constructor

        Args:
            root (Node, optional): Node to be assigned as root
        """
        self.root = root

    def pre_order(self) -> list:
        """Return a list of values in root >> left >> right order

        Returns:
            list: List of values
        """
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
        """Return a list of values in left >> root >> right order

        Returns:
            list: List of values
        """
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
        """Return a list of values in left >> right >> root 

        Returns:
            list: List of values
        """
        result = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            result.append(root.value)
        traverse(self.root)
        return result

    def find_maximum_value(self):
        max_value = self.root.value
        def traverse(root):
            nonlocal max_value
            if root.value > max_value:
                max_value = root.value
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        traverse(self.root)
        return max_value

class BinarySearchTree(BinaryTree):
    """Binary Search Tree class. Inherits from BinaryTree.
    """
    def add(self, value):
        """Add a value to the tree

        Args:
            value (any): value to add
        """
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
        """Checks if given value exists in the tree

        Args:
            value (any): value to check

        Returns:
            bool: True if value exists
        """
        root = self.root
        while root:
            if root.value == value:
                return True
            elif value < root.value:
                root = root.left
            elif value > root.value:
                root = root.right
        return False
