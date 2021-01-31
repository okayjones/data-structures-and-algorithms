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
        # root = self.root

        # if not root:
        #     self.root = Node(value)

        # while root:
        #     if value < root.value:
        #         if not root.left:
        #             root.left = Node(value)
        #             break
        #         root = root.left

        #     elif value > root.value:                
        #         if not root.right:
        #             root.right = Node(value)
        #             break
        #         root = root.right
        
        if not self.root:
            self.root = Node(value)

        def traverse(root):
            if value < root.value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    traverse(root.left)
            elif value > root.value:
                if root.right is None:
                    root.right = Node(value)
                else:
                    traverse(root.right)

        traverse(self.root)



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


if __name__ == '__main__':
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

    print(tree.pre_order())
    print(tree.add(15))
    print(tree.pre_order())
