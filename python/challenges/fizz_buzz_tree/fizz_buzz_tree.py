def fizz_buzz_tree(tree):
    def traverse(root):
        root.value = fizz_buzz(root.value)
        if root.left:
            traverse(root.left)
        if root.right:
            traverse(root.right)
    traverse(self.root)

    def fizz_buzz(value):
        if value % 15:
            return 'FizzBuzz'
        elif value % 3:
            return 'Fizz'
        elif value % 5:
            return 'Buzz'
        else:
            return str(value)

    return tree